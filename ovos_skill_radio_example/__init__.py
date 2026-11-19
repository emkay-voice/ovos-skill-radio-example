"""Your own radio: say "play Emkay Chill" and it plays.

A media skill: there are no intents. When someone says "play …", OpenVoiceOS'
media player (OCP) asks every media skill what it has for that
(search_radio) and plays the best match – a station, a song, a podcast.
Here: the internet radio stations in STATIONS, from SomaFM (listener-
supported radio, https://somafm.com), under names of their own – Emkay
Chill, Emkay Space, Emkay Lounge – so no other media skill has a station by
the same name (on a tie, the first answer wins). "play some radio"
(radio.voc) offers them all.

Try changing: STATIONS – any stream address works; what counts as a match
(MATCH, and the station's own words in "words"); or add a picture.
"""
from difflib import SequenceMatcher

from ovos_utils.ocp import MediaEntry, MediaType, PlaybackType
from ovos_workshop.decorators.ocp import ocp_featured_media, ocp_search
from ovos_workshop.skills.common_play import OVOSCommonPlaybackSkill

#: (name, other words for it, the stream, a picture)
STATIONS = [
    ("Emkay Chill", ["groove", "chill", "ambient beats"], "https://ice2.somafm.com/groovesalad-128-mp3",
     "https://somafm.com/img3/groovesalad-400.jpg"),
    ("Emkay Space", ["drone", "ambient", "space"], "https://ice2.somafm.com/dronezone-128-mp3",
     "https://somafm.com/img3/dronezone-400.jpg"),
    ("Emkay Lounge", ["spy", "lounge", "jazz"], "https://ice2.somafm.com/secretagent-128-mp3",
     "https://somafm.com/img3/secretagent-400.jpg"),
]
MATCH = 0.8   # how alike the words must be to a station's name, 0..1


def words(text):
    return " ".join("".join(c if c.isalnum() else " " for c in (text or "").lower()).split())


def score(phrase, name, others):
    """How sure we are that `phrase` asks for this station, 0..100."""
    p = f" {words(phrase)} "
    if f" {words(name)} " in p:
        return 100        # its whole name: this is the one (and beats a general radio search)
    best = max(SequenceMatcher(None, words(phrase), words(n)).ratio() for n in [name, *others])
    if any(f" {words(o)} " in p for o in others):
        best = max(best, 0.8)
    return int(best * 100) if best >= MATCH else 0


class RadioSkill(OVOSCommonPlaybackSkill):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, supported_media=[MediaType.RADIO, MediaType.MUSIC, MediaType.GENERIC], **kwargs)

    def entry(self, station, confidence, media_type=MediaType.RADIO):
        name, _, stream, picture = station
        return MediaEntry(uri=stream, title=name, artist="SomaFM", image=picture,
                          media_type=media_type, playback=PlaybackType.AUDIO,
                          match_confidence=confidence, skill_id=self.skill_id)

    @ocp_search()
    def search_radio(self, phrase, media_type=MediaType.GENERIC):
        """What we have for "play <phrase>": each station that matches, how sure (0..100)."""
        found = [(score(phrase, s[0], s[1]), s) for s in STATIONS]
        found = [(c, s) for c, s in found if c]
        if not found and self.voc_match(phrase, "radio"):
            found = [(60, s) for s in STATIONS]          # "play some radio": all of them
        # OCP guesses from the sentence what kind of media is wanted and drops
        # every answer of another kind: a name it doesn't know ("emkay chill")
        # is often heard as music. Radio plays music, so answer as that kind.
        kind = media_type if media_type in (MediaType.RADIO, MediaType.MUSIC) else MediaType.RADIO
        return [self.entry(s, c, kind) for c, s in sorted(found, key=lambda x: -x[0])]

    @ocp_featured_media()
    def featured(self):
        """What the media player shows when you look at this skill."""
        return [self.entry(s, 100) for s in STATIONS]

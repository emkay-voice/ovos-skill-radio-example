"""Quick checks that run without OpenVoiceOS running: `pytest`.

Talking to the skill is the real test - in Emkay (Emkay: Test the skill)
or with ovos-tui-client against an OVOS - but these catch the usual slips
early: a language missing a file, or an intent with no answer.
"""
import json
import sys
from pathlib import Path

from ovos_bus_client.message import Message
from ovos_utils.fakebus import FakeBus

ROOT = Path(__file__).parent.parent
PACKAGE = ROOT / "ovos_skill_radio_example"
sys.path.insert(0, str(ROOT))
import ovos_skill_radio_example as pkg  # noqa: E402

SKILL_ID = "ovos-skill-radio-example.emkay-voice"
LANGS = sorted(p.name for p in (PACKAGE / "locale").iterdir() if p.is_dir())


def test_every_language_has_the_same_files():
    first = sorted(f.name for f in (PACKAGE / "locale" / LANGS[0]).iterdir())
    for lang in LANGS[1:]:
        assert sorted(f.name for f in (PACKAGE / "locale" / lang).iterdir()) == first, lang


def test_golden_utterances_are_for_this_skill():
    for f in (ROOT / "test" / "end2end").glob("golden_utterances_*.jsonl"):
        for line in f.read_text().splitlines():
            if line.strip():
                assert json.loads(line)["skill_id"] == SKILL_ID, f.name


def test_a_station_by_its_name_and_its_words():
    groove = pkg.STATIONS[0]
    assert pkg.score("play emkay chill", groove[0], groove[1]) == 100
    assert pkg.score("play something chill", groove[0], groove[1]) >= 80
    assert pkg.score("play the news", groove[0], groove[1]) == 0


def test_every_language_has_the_word_radio():
    for lang in LANGS:
        assert (PACKAGE / "locale" / lang / "radio.voc").read_text().strip(), lang

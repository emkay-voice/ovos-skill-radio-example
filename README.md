# Your own radio

Say **"play Emkay Chill"** and it plays: a media skill for OpenVoiceOS'
media player (OCP), with three internet radio stations from
[SomaFM](https://somafm.com) – in all twelve of [Emkay](https://emkay.ai)'s
languages.

**👉 The friendly guide: <https://dev.emkay.ai>**

## What it shows

- **Media, no intents:** "play …" goes to OpenVoiceOS' media player, which
  asks every media skill what it has (`@ocp_search` → `search_radio`) and
  plays the best match. You return `MediaEntry`s – the stream, a title, a
  picture and how sure you are (0–100).
- **Featured media:** `@ocp_featured_media` lists what the skill offers, for
  the media player's screen.
- **A word per language:** "play some radio" finds `radio.voc`'s words in the
  sentence, and offers all the stations.

## Try changing

- `STATIONS` – any stream address works: your local station, a podcast feed's
  episodes, your own music server;
- `MATCH` and each station's own words – what counts as asking for it.

SomaFM is listener-supported: if you like it, <https://somafm.com/support/>.

## A working skill, and a template

This is a complete OpenVoiceOS skill – install it and it works – and an
example to start your own from: *Use this template* on GitHub, or
*Emkay: New skill* in VS Code ([Emkay Dev](https://dev.emkay.ai)), which
gives it your own names. Made for [Emkay](https://emkay.ai), it runs on any
OpenVoiceOS.

## Try it

- **Emkay Dev (VS Code):** *Emkay: Run the skill in Emkay* (Ctrl+Alt+E) opens
  Emkay next to your code and loads the skill; type under Emkay to talk to it.
  Every save loads it again. *Emkay: Test the skill* sends the golden
  utterances and shows ✓ / ✗ in the Testing view. Emkay's menu →
  *Guardian* → *What's happening?* shows which skill took a sentence, and why.
- **ovos-tui-client (Codespaces, Dev Container):** run `ovos-tui` in the
  terminal, type to talk, `Ctrl+P` → *Test* runs the same golden utterances
  against a full OpenVoiceOS.
- **pytest:** `pytest -q` – no OpenVoiceOS needed.

When you make a repository from this template ("Use this template"), a
small workflow renames the skill after your repository and then removes
itself.

## Show it, on your own Emkay, and into the store

To show it in [See my skill](https://dev.emkay.ai/#gallery) on dev.emkay.ai –
ready or not – add the topic `emkay-skill` to the repository (the ⚙ next to
*About*). Remove the topic, or make the repository private, to take it away.

*Emkay: Send to my Emkay* shows a QR code that installs this skill from
GitHub on the Emkay you scan it with. To get it into the
[Emkay store](https://store.emkay.ai): topics `ovos` and `openvoiceos` on the
repository, a release on GitHub (`publish.yml` puts it on PyPI), and the
store's nightly test does the rest – <https://dev.emkay.ai/#store>.

More on writing skills:
[the OpenVoiceOS technical manual](https://openvoiceos.github.io/ovos-technical-manual/).

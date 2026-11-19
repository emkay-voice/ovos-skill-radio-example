#!/bin/bash
# Installs a text-only OpenVoiceOS and this skill (editable: your changes count
# at the next restart of OVOS), plus ovos-tui-client. Runs once, when the
# container is made.
set -e
pip install --quiet --upgrade pip
pip install --quiet --pre ovos-messagebus "ovos-core[plugins]" ovos-tui-client
pip install --quiet -e ".[test]"
echo
echo "Ready. In the terminal:"
echo "  ovos-tui                 talk to OpenVoiceOS, and test your skill (Ctrl+P → test)"
echo "  bash .devcontainer/ovos.sh restart   after changing the skill"

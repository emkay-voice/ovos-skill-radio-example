#!/bin/bash
# Start, stop or restart the text-only OpenVoiceOS in this container:
#   bash .devcontainer/ovos.sh start|stop|restart
# Logs: ~/.local/state/mycroft/*.log (ovos-tui-client shows them too)
LOGS=~/.local/state/mycroft
mkdir -p "$LOGS"
stop() { pkill -f ovos-messagebus 2>/dev/null; pkill -f ovos-core 2>/dev/null; sleep 1; }
start() {
  nohup ovos-messagebus > "$LOGS/bus.log" 2>&1 &
  sleep 2
  nohup ovos-core > "$LOGS/skills.log" 2>&1 &
  echo "OpenVoiceOS is starting (skills load in ~20 s). Talk to it: ovos-tui"
}
case "$1" in
  stop) stop ;;
  restart) stop; start ;;
  *) start ;;
esac

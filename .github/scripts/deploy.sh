#!/usr/bin/env bash
set -eu

#trap catch ERR

# if you need error nortify to mattermost, you need to create notify_mattermost.sh
#function catch {
#    bash .github/scripts/notify_mattermost.sh Deploy FAILED
#}

#deploy
./ecspresso deploy --config=.github/ecspresso/"${ECS_ENV}"/config.yml
#bash .github/scripts/notify_mattermost.sh Deploy SUCCEEDED

# RocketChat extension for Zammad

This extension can be installed on a Zammad instance

## License

AGPL-3.0

## Generating zammad package

python3 create-zammad-extension.py > zammad-rocketchat.szpm

## Installing extension

* install package in zammad
* add *rocket* to seeds variable in file db/seeds.rb on rails server

    seeds = %w[settings user_nr_1 signatures roles permissions groups links ticket_state_types ticket_states ticket_priorities ticket_article_types ticket_article_senders macros community_user_resources overviews channels report_profiles chats object_manager_attributes schedulers triggers karma_activities rocket]

* and execute the following commands:

    RAILS_ENV=production rake db:seed
    RAILS_ENV=production rake assets:precompile

* Restart rails server, scheduler and nginx processes/containers
* Refresh your brower to avoid cache

Now rocket appears in integration menu and can be configured and activated.

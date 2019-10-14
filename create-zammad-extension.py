import os
import base64

template = '''{
  "name": "RocketChat for Zammad",
  "version": "1.0.0",
  "vendor": "GenOuest",
  "license": "MIT",
  "url": "https://www.genouest.org",
  "buildhost": "",
  "builddate": "2019-10-11 14:59:00 UTC",
  "change_log": [
    {
      "version": "1.0.0",
      "date": "2019-10-11 14:59:00 UTC",
      "log": "Initial version."
    }
  ],
  "description": [
    {
      "language": "en",
      "text": "Adding Zammad to RocketChat notifications and mentions"
    }
  ],
  "files": [
  %s
  ]
}'''

files = [
    'app/assets/javascripts/app/controllers/_integration/rocketchat.coffee',
    'app/models/transaction/rocketchat.rb',
    'app/views/rocketchat/application.md.erb',
    'app/views/rocketchat/ticket_create/en.md.erb',
    'app/views/rocketchat/ticket_create/pt-br.md.erb',
    'app/views/rocketchat/ticket_create/zh-cn.md.erb',
    'app/views/rocketchat/ticket_create/zh-tw.md.erb',
    'app/views/rocketchat/ticket_escalation/en.md.erb',
    'app/views/rocketchat/ticket_escalation/pt-br.md.erb',
    'app/views/rocketchat/ticket_escalation/zh-cn.md.erb',
    'app/views/rocketchat/ticket_escalation/zh-tw.md.erb',
    'app/views/rocketchat/ticket_escalation_warning/en.md.erb',
    'app/views/rocketchat/ticket_escalation_warning/pt-br.md.erb',
    'app/views/rocketchat/ticket_escalation_warning/zh-cn.md.erb',
    'app/views/rocketchat/ticket_escalation_warning/zh-tw.md.erb',
    'app/views/rocketchat/ticket_mentioned/en.md.erb',
    'app/views/rocketchat/ticket_reminder_reached/en.md.erb',
    'app/views/rocketchat/ticket_reminder_reached/pt-br.md.erb',
    'app/views/rocketchat/ticket_reminder_reached/zh-cn.md.erb',
    'app/views/rocketchat/ticket_reminder_reached/zh-tw.md.erb',
    'app/views/rocketchat/ticket_update/en.md.erb',
    'app/views/rocketchat/ticket_update/pt-br.md.erb',
    'app/views/rocketchat/ticket_update/zh-cn.md.erb',
    'app/views/rocketchat/ticket_update/zh-tw.md.erb',
    'lib/notification_factory/rocketchat.rb',
    'spec/lib/notification_factory/rocketchat_spec.rb',
    'db/seeds/rocket.rb'
    ]

tplfile = '''{
      "location": "%s",
      "permission": 644,
      "encode": "base64",
      "content": "%s"
}
'''

tplfiles = []
for f in files:
    with open(f) as t:
        content = t.read()
        b64 = base64.b64encode(str.encode(content))
        tplfiles.append(tplfile % (f, b64.decode()))
print(template % (','.join(tplfiles)))

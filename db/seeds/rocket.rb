
Setting.create_if_not_exists(
  title:       'Defines transaction backend.',
  name:        '7000_rocketchat_webhook',
  area:        'Transaction::Backend::Async',
  description: 'Defines the transaction backend which posts messages to Rocketchat.',
  options:     {},
  state:       'Transaction::Rocketchat',
  frontend:    false
)
Setting.create_if_not_exists(
  title:       'Rocketchat integration',
  name:        'rocketchat_integration',
  area:        'Integration::Switch',
  description: 'Defines if Rocketchat is enabled or not.',
  options:     {
    form: [
      {
        display: '',
        null:    true,
        name:    'rocketchat_integration',
        tag:     'boolean',
        options: {
          true  => 'yes',
          false => 'no',
        },
      },
    ],
  },
  state:       false,
  preferences: {
    prio:       1,
    permission: ['admin.integration'],
  },
  frontend:    false
)
Setting.create_if_not_exists(
  title:       'Rocketchat config',
  name:        'rocketchat_config',
  area:        'Integration::Rocketchat',
  description: 'Defines the rocketchat config.',
  options:     {},
  state:       {
    items: []
  },
  preferences: {
    prio:       2,
    permission: ['admin.integration'],
  },
  frontend:    false,
)

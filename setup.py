"""
	setup
		repository directory
		my own file status tracker
		setup plugins
		reactor details
"""

import queue

queue.define_rules("crypto",
    [ queue.PhysicsRule(f"plugin.{crypto_plugin}", "crypto", None, "ignore")
    , queue.PhysicsRule(f"plugin.{backup_plugin}", "backup", None, "ignore") ]) # it would be nice if crypto_plugin.crypto's return value could be added to all_params pool fir backup_plugin.backup

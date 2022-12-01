### DQN block_arrangement Config ###

env = {
    "name": "block_arrangement",
    "stock_scale": 3,
    "utilization": 70,
    "width": 6,
    "height": 5,
    "block_size" : 1,
    "num_blocks": 20,
    "provided_ratio": 1,
    "entrance_cnt": 1,
    "entrance_position": [5,0],
    "rearrangement_occur_reward": -5,
    "arrangement_fail_reward": -1,
    "schedule_clear_reward_without_rearrangement": +1
}

agent = {
    "name": "dqn",
    "network": "discrete_q_network",
    "head": "mlp",
    "gamma": 0.99,
    "epsilon_init": 1.0,
    "epsilon_min": 0,
    "explore_ratio": 0.2,
    "buffer_size": 10000,
    "batch_size": 32,
    "start_train_step": 2000,
    "target_update_period": 500,
    "lr_decay": True,
}

optim = {
    "name": "adam",
    "lr": 1e-4,
}

train = {
    "training": True,
    "load_path": None,
    "run_step": 100000,
    "print_period": 2000,
    "save_period": 2000,
    "eval_iteration": 5,
    "record": True,
    "record_period": 2000,
    # distributed setting
    "update_period": 32,
    "num_workers": 16,
}

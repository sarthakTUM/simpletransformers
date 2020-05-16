from multiprocessing import cpu_count

global_args = {
    "adam_epsilon": 1e-8,
    "best_model_dir": "outputs/best_model",
    "cache_dir": "cache_dir/",
    "config": {},
    "do_lower_case": False,
    "early_stopping_consider_epochs": False,
    "early_stopping_delta": 0,
    "early_stopping_metric": "eval_loss",
    "early_stopping_metric_minimize": True,
    "early_stopping_patience": 3,
    "encoding": None,
    "eval_batch_size": 8,
    "fp16": True,
    "fp16_opt_level": "O1",
    "gradient_accumulation_steps": 1,
    "learning_rate": 4e-5,
    "logging_steps": 50,
    "save_during_training": False,
    "save_steps": 2000,
    "no_cache": False,
    "save_model_every_epoch": True,
    "evaluate_during_training": False,
    "evaluate_during_training_steps": 2000,
    "evaluate_during_training_verbose": False,
    "evaluate_after_every_epoch": True,
    "evaluate_after_every_epoch_verbose": True,
    "use_cached_eval_features": False,
    "save_eval_checkpoints": True,
    "tensorboard_dir": None,
    "manual_seed": None,
    "max_grad_norm": 1.0,
    "max_seq_length": 128,
    "n_gpu": 1,
    "num_train_epochs": 1,
    "output_dir": "outputs/",
    "overwrite_output_dir": False,
    "process_count": cpu_count() - 2 if cpu_count() > 2 else 1,
    "reprocess_input_data": True,
    "save_best_model": True,
    "silent": False,
    "wandb_project": None,
    "wandb_kwargs": {},
    "use_early_stopping": True,
    "train_batch_size": 8,
    "use_multiprocessing": True,
    "warmup_ratio": 0.06,
    "warmup_steps": 0,
    "weight_decay": 0
}

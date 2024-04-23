import numpy as np

def generate_params():
    params = {
        'batch_size': int(np.random.choice([256, 512, 1024])),
        'n_epochs': int(np.random.choice([20, 15, 25])),
        'pct_start': float(np.random.uniform(0.3, 0.5)),
        'weight_decay': float(np.random.uniform(0.01, 0.3)),
        'dropout': float(np.random.choice([0.8, 0.9, 0.75])),
        'max_lr': float(np.random.uniform(0.00003, 0.00007)),
        'use_lr_scheduler': int(np.random.choice([0, 1])),
        'use_hidden_layer': int(np.random.choice([0, 1])),
        'train_data': 'both',
        'sample_ratio': float(np.random.choice([0.1, 0.25, 0.5, 0.75, 1.0])),
    }
    return params

def submit(params, scheduler_config='scheduler', job_directory='.', command='main.py', stream_job_logs=False):
    return f"Scheduler Config: {scheduler_config}, Job Directory: {job_directory}, Command: {command}, Params: {params}, Stream Job Logs: {stream_job_logs}"
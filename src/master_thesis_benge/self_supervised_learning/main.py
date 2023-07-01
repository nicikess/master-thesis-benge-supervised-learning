import wandb
import torch
import numpy as np

from master_thesis_benge.self_supervised_learning.config.constants import (
    TASK_KEY,
    TRAINING_CONFIG_KEY,
    SENTINEL_1_INDEX_KEY,
    CLIMATE_ZONE_INDEX_KEY,
    ERA_5_INDEX_KEY,
    SEASON_S2_INDEX_KEY,
    GLO_30_DEM_INDEX_KEY,
    SENTINEL_2_INDEX_KEY,
    ESA_WORLD_COVER_INDEX_KEY,
    TASK_CONFIG_KEY,
    PIPELINES_CONFIG_KEY,
    TRAINING_RESNET_CONFIG_KEY,
    TRAINING_UNET_CONFIG_KEY,
    EVALUATION_CLASSIFICATION_LANDUSE_MULTILABEL_CONFIG_KEY,
    EVALUATION_SEGMENTATION_LANDUSE_CONFIG_KEY
)

from master_thesis_benge.self_supervised_learning.training.train import training

from master_thesis_benge.self_supervised_learning.evaluation.evaluation import evaluation

from ffcv.loader import Loader, OrderOption

if __name__ == "__main__":

    # Train SSL
    def train_setup():

        training_config = TRAINING_UNET_CONFIG_KEY

        sweep_configuration = {
            "method": "grid",
            "name": "train-ssl-sen2-sen1-60-delta",
            "parameters": {
                "training_config": {"values": [training_config]},
                "batch_size": {"values": [128]},
                "temperature": {"values": [0.1]},
                "dataset_size": {'values': ["60-delta-multilabel"]},
                "modalities": {'values':    [
                                                [SENTINEL_2_INDEX_KEY, SENTINEL_1_INDEX_KEY],
                                            ]
                            },
            },
        }

        if training_config == TRAINING_RESNET_CONFIG_KEY:
            project_name = "master-thesis-ssl-training-resnet"
        elif training_config == TRAINING_UNET_CONFIG_KEY:
            project_name = "master-thesis-ssl-training-unet"

        sweep_id = wandb.sweep(
            sweep=sweep_configuration, project=project_name
        )

        wandb.agent(sweep_id, function=training)


    def evaluation_setup():

        pre_trained_weights =   [
                                    'saved_models/resnet_weights/lxfkckti/sentinel2-sentinel1-60-delta-multilabel.ckpt',
                                ]
    
        modalities =            [
                                    [SENTINEL_2_INDEX_KEY, SENTINEL_1_INDEX_KEY],
                                ]
        
        sweep_name =            [
                                    'sentinel2-sentinel1',
                                ]
        
        evaluation_task = EVALUATION_CLASSIFICATION_LANDUSE_MULTILABEL_CONFIG_KEY
        
        for i in range(len(pre_trained_weights)):
            sweep_configuration = {
                "method": 'grid',
                "name": sweep_name[i],
                "parameters": {
                    "evaluation_config": {'values': [evaluation_task]},
                    "seed": {'values': [42]},
                    "batch_size": {"values": [128]}, # only to init the SimCLR model
                    "temperature": {"values": [0.1]},  # only to init the SimCLR model
                    "pre_trained_weights_path": {'values': [pre_trained_weights[i]]},
                    "modalities": {'values':    [modalities[i]]
                                },
                }
            }

            if evaluation_task == EVALUATION_CLASSIFICATION_LANDUSE_MULTILABEL_CONFIG_KEY:
                project_name = 'master-thesis-ssl-evaluation-classification-landuse-multilabel'
            elif evaluation_task == EVALUATION_SEGMENTATION_LANDUSE_CONFIG_KEY:
                project_name = 'master-thesis-ssl-evaluation-segmentation-landuse'

            sweep_id = wandb.sweep(sweep=sweep_configuration, project=project_name)
            wandb.agent(sweep_id, function=evaluation)

    
    # Train
    #train_setup()

    # Evaluate
    evaluation_setup()
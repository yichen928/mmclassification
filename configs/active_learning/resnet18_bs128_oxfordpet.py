_base_ = [
     '../_base_/datasets/OxfordPet_bs128.py', '../_base_/default_runtime.py', '../_base_/models/resnet18.py',
]

# load model pretrained on imagenet
model = dict(
    backbone=dict(
        init_cfg=dict(
            type='Pretrained',
            checkpoint='https://download.openmmlab.com/mmclassification/v0/resnet/resnet18_batch256_imagenet_20200708-34ab8f90.pth',
            prefix='backbone',
        )),
    head=dict(num_classes=37),
)

# optimizer
optimizer = dict(
    type='SGD',
    lr=0.01,
    momentum=0.9,
    weight_decay=1e-4
)
optimizer_config = dict(grad_clip=None)
# learning policy
lr_config = dict(policy='CosineAnnealing', min_lr=0)
runner = dict(type='EpochBasedRunner', max_epochs=60)

log_config = dict(
    interval=1,
    hooks=[
        dict(type='TextLoggerHook'),
        # dict(type='TensorboardLoggerHook')
    ])

checkpoint_config = dict(interval=60)

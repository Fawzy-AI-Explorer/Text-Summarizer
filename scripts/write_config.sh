#!/usr/bin/env bash

# Target path
config_path="LLaMA-Factory/examples/train_lora/summary_finetune.yaml"

# Write the YAML content
cat <<EOF > "$config_path"
### model
model_name_or_path: Qwen/Qwen2.5-0.5B-Instruct
trust_remote_code: true

### method
stage: sft
do_train: true
finetuning_type: lora
lora_rank: 8
lora_target: all
lora_dropout: 0.1

### dataset
dataset: summary_finetune_train
eval_dataset: summary_finetune_val
template: qwen
cutoff_len: 3500
# max_samples: 50
overwrite_cache: true
preprocessing_num_workers: 16

### output
output_dir: /teamspace/studios/this_studio/Text-Summarization/models/finetuned
logging_steps: 10
save_steps: 500
plot_loss: true
# overwrite_output_dir: true

### train
per_device_train_batch_size: 4
gradient_accumulation_steps: 2
learning_rate: 2.0e-4
num_train_epochs: 10
lr_scheduler_type: cosine
warmup_ratio: 0.1
bf16: true
ddp_timeout: 1800

### eval
# val_size: 0.1
per_device_eval_batch_size: 4
eval_strategy: steps
eval_steps: 500
logging_strategy: steps
logging_steps: 500

report_to: wandb
run_name: summary-finetune-llamafactory
load_best_model_at_end: true
metric_for_best_model: eval_loss

push_to_hub: true
export_hub_model_id: "mohammedfawzy/Text_Summarization"
hub_private_repo: true
hub_strategy: checkpoint
EOF

echo "✅ Config file written to: $config_path"
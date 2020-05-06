export BERT_BASE_DIR="./pre_trained_model/uncased_L-12_H-768_A-12"
export DATA_DIR="./data"

python ./bert/run_classifier.py \
  --task_name=EnSent \
  --do_train=True \
  --do_eval=True \
  --data_dir=$DATA_DIR \
  --vocab_file=$BERT_BASE_DIR/vocab.txt \
  --bert_config_file=$BERT_BASE_DIR/bert_config.json \
  --init_checkpoint=$BERT_BASE_DIR/bert_model.ckpt \
  --train_batch_size=32 \
  --learning_rate=2e-5 \
  --num_train_epochs=3.0 \
  --max_seq_length=64 \
  --output_dir=./output
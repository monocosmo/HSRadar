export BERT_BASE_DIR="./pre_trained_model/uncased_L-12_H-768_A-12"
export DATA_DIR="./data"

python ./bert/run_classifier.py \
  --task_name=EnSent \
  --do_predict=True \
  --data_dir=$DATA_DIR \
  --vocab_file=$BERT_BASE_DIR/vocab.txt \
  --bert_config_file=$BERT_BASE_DIR/bert_config.json \
  --init_checkpoint=./output \
  --max_seq_length=64 \
  --output_dir=./prediction
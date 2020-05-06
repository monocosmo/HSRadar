import pandas as pd

def classify(list_normal, list_hate):
  result = []
  for i in range(len(list_hate)):
    if list_hate[i] >= list_normal[i]:
      result.append(1)
    else:
      result.append(0)
  return result

if __name__ == '__main__':
  result_df = pd.read_csv("./raw_results/en2_test_results.tsv", sep="\t", header=None)
  result_df.columns = ["normal", "hate"]
  list_normal = result_df.normal
  list_hate = result_df.hate
  classify_result = classify(list_normal, list_hate)
  data_df = pd.read_csv("./en2.csv", sep="\t")
  classify_df = pd.DataFrame({'tweet':data_df.review, 'normal': list_normal, 'hate': list_hate, 'classify': classify_result})
  classify_df.to_csv("./en2_classify.csv", index=False, sep='\t')
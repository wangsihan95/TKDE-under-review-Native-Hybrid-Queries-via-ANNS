import numpy as np
import pandas as pd


def csv_view(outputfile):
    data = pd.read_csv(outputfile, header=None)
    print("data shape: ", data.shape)
    rows = data.shape[0]
    print("rows: ", rows)
    print("head: ")
    print(data.head())
    # data.head().to_csv('output_sample.csv', index=False)


def fvecs_add_random_int_column(inputfile, outputfile):
    a = np.fromfile(inputfile, dtype='int32')
    d = a[0]  # dim
    print("dim: ", d)
    # Reshape array a into a new two-dimensional array with the second dimension of size d + 1
    # the first dimension automatically resized.
    new = a.reshape(-1, d + 1)
    rows = (len(a)) // (d + 1)
    random_ints = np.random.randint(low=1, high=10, size=rows).astype('int32')
    new = np.hstack((new, random_ints[:, np.newaxis]))
    if outputfile.endswith('.csv'):
        print("write to csv file")
        new_df = pd.DataFrame(new)
        new_df.to_csv(outputfile, index=False, header=False)
    else:
        print("write to fvecs file")
        new.tofile(outputfile)
    print("finish!")


if __name__ == "__main__":
    input = "/home/wangsihan/datasets/datasets/sift1M/sift_base.fvecs"
    output_csv = "./sift_base_with_random_int_added.csv"
    output_fvecs = "./sift_base_with_random_int_added.fvecs"

    # dataset = fvecs_add_random_int_column(input, output_csv)
    csv_view(output_csv)

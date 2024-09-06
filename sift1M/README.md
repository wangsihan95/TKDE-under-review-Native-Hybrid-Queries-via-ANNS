**#** **数据描述**

### 1. 数据描述

base_datasets：./sift_base_with_random_int_added.csv

query: ./example_query.png

> sift_base_with_random_int_added.csv和.fvecs完全对齐：行列序号为自动添加忽略，第一列为维度，最后一列为添加的1~10的标签，用于混合查询中的精准匹配，中间为128维的向量
>
> 见output_sample.csv

运行python3 add_random_int_column.py 查看数据规格

- csv_view函数查看数据规格  
- 已打印输出到output_sample.csv


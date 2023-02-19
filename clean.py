import pandas as pd

def clean(input_file1, input_file2):
    df1 = pd.read_csv(input_file1)
    df2 = pd.read_csv(input_file2)
    df = pd.merge(df1, df2, left_on='respondent_id', right_on='id')
    df.drop('id', axis=1, inplace=True)
    df = df.dropna()
    df = df[df['job'].str.contains('insurance|Insurance')==False]
    return df


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('input1', help='contact_info_file (CSV)')
    parser.add_argument('input2', help='other_info_file (CSV)')
    parser.add_argument('output', help='Cleaned output_file (CSV)')
    args = parser.parse_args()

    cleaned = clean(args.input1, args.input2)

    cleaned.to_csv(args.output, index=False)


# check the shape of the output file
print(cleaned.shape)
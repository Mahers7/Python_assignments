import pandas as pd

def read_excel(file_path):
    return pd.read_excel(file_path)

def compute_statistics(df):
    naive_cols = [f'Na_{i}' for i in range(1, 4)]
    injured_cols = [f'Inj_{i}' for i in range(1, 4)]

    df['Naive_Mean'] = df[naive_cols].mean(axis=1).round(2)
    df['Naive_SD'] = df[naive_cols].std(axis=1).round(2)
    df['Injured_Mean'] = df[injured_cols].mean(axis=1).round(2)
    df['Injured_SD'] = df[injured_cols].std(axis=1).round(2)
    return df

def save_to_excel(df, output_path):
    df.to_excel(output_path, index=False)

if __name__ == '__main__':
    input_file = 'rnaseq.xlsx'
    output_file = 'rnaseq_processed.xlsx'
    
    df = read_excel(input_file)
    df = compute_statistics(df)
    save_to_excel(df, output_file)
    
    print("Computation complete. Results saved to:", output_file)
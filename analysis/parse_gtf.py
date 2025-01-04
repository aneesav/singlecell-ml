import pandas as pd

# Define column names for the GTF file
columns = [
    'seqname', 'source', 'feature', 'start', 'end', 'score', 'strand', 'frame', 'attribute'
]

# Read the GTF file into a DataFrame
gtf = pd.read_csv('/Users/aneesavalentine/Desktop/Homo_sapiens.GRCh38.113.gtf', sep='\t', comment='#', names=columns)

# Filter for transcript features
transcripts = gtf[gtf['feature'] == 'transcript']

# Parse the attribute column to extract transcript_id and gene_id
transcripts['transcript_id'] = transcripts['attribute'].str.extract('transcript_id "([^"]+)"')
transcripts['gene_id'] = transcripts['attribute'].str.extract('gene_id "([^"]+)"')

# Select relevant columns
transcript_info = transcripts[['gene_id', 'transcript_id', 'seqname', 'start', 'end', 'strand']]

# Save to .csv
transcript_info.to_csv('transcript_info.csv', index=False)

# Display the first few rows
print(transcript_info.head())

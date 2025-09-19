"""
Download sample PDFs for testing the RAG system
"""
import os
import requests
from typing import List, Dict
from tqdm import tqdm


class SamplePDFDownloader:
    """Downloads sample PDFs for testing"""
    
    # Sample PDFs (publicly available documents)
    SAMPLE_PDFS = [
        {
            "name": "attention_is_all_you_need.pdf",
            "url": "https://arxiv.org/pdf/1706.03762.pdf",
            "description": "Transformer paper"
        },
        {
            "name": "bert_paper.pdf",
            "url": "https://arxiv.org/pdf/1810.04805.pdf",
            "description": "BERT paper"
        },
        {
            "name": "gpt_paper.pdf",
            "url": "https://arxiv.org/pdf/2005.14165.pdf",
            "description": "GPT-3 paper"
        }
    ]
    
    def __init__(self, download_dir: str = "./data/raw"):
        self.download_dir = download_dir
        os.makedirs(download_dir, exist_ok=True)
    
    def download_pdf(self, url: str, filename: str) -> bool:
        """Download a single PDF"""
        try:
            response = requests.get(url, stream=True, timeout=30)
            response.raise_for_status()
            
            filepath = os.path.join(self.download_dir, filename)
            total_size = int(response.headers.get('content-length', 0))
            
            with open(filepath, 'wb') as file:
                with tqdm(
                    desc=filename,
                    total=total_size,
                    unit='B',
                    unit_scale=True,
                    unit_divisor=1024,
                ) as pbar:
                    for chunk in response.iter_content(chunk_size=8192):
                        file.write(chunk)
                        pbar.update(len(chunk))
            
            return True
        except Exception as e:
            print(f"Error downloading {filename}: {str(e)}")
            return False
    
    def download_all_samples(self) -> List[str]:
        """Download all sample PDFs"""
        downloaded = []
        
        print(f"Downloading sample PDFs to: {os.path.abspath(self.download_dir)}\n")
        
        for pdf_info in self.SAMPLE_PDFS:
            filepath = os.path.join(self.download_dir, pdf_info['name'])
            
            # Skip if already exists
            if os.path.exists(filepath):
                print(f"✓ {pdf_info['name']} already exists")
                downloaded.append(pdf_info['name'])
                continue
            
            print(f"Downloading {pdf_info['description']}...")
            if self.download_pdf(pdf_info['url'], pdf_info['name']):
                downloaded.append(pdf_info['name'])
                print(f"✓ Downloaded {pdf_info['name']}\n")
            else:
                print(f"✗ Failed to download {pdf_info['name']}\n")
        
        return downloaded


def main():
    """Download sample PDFs"""
    downloader = SamplePDFDownloader()
    downloaded_files = downloader.download_all_samples()
    
    print(f"\nDownloaded {len(downloaded_files)} PDF files:")
    for file in downloaded_files:
        print(f"  - {file}")
    
    print(f"\nPDFs saved to: {os.path.abspath(downloader.download_dir)}")


if __name__ == "__main__":
    main()

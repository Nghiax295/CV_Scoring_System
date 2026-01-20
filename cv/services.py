import PyPDF2
import logging
import re

logger = logging.getLogger(__name__)


def extract_text_from_pdf(cv_instance):
    """
    Trích xuất text từ file PDF CV.
    
    Args:
        cv_instance: Instance của model CV
        
    Returns:
        str: Text được trích xuất, hoặc empty string nếu thất bại
    """
    try:
        # Mở file PDF
        with open(cv_instance.file.path, 'rb') as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            
            # Duyệt qua từng trang và trích xuất text
            text = []
            for page in pdf_reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text.append(page_text)
            
            # Nối tất cả text lại
            extracted = '\n'.join(text)
            logger.info(f"Successfully extracted text from CV {cv_instance.id}, length: {len(extracted)}")
            return extracted
            
    except Exception as e:
        logger.error(f"Error extracting text from CV {cv_instance.id}: {str(e)}")
        return ""


def preprocess_text(text):
    """
    Tiền xử lý văn bản CV.
    
    Args:
        text: Text cần xử lý
        
    Returns:
        str: Text đã được làm sạch
    """
    if not text:
        return ""
    
    try:
        # Chuyển về lowercase
        text = text.lower()
        
        # Loại bỏ ký tự đặc biệt, giữ lại chữ cái, số và khoảng trắng
        text = re.sub(r'[^a-z0-9\s]', ' ', text)
        
        # Loại bỏ khoảng trắng thừa
        text = re.sub(r'\s+', ' ', text)
        
        # Trim
        text = text.strip()
        
        logger.info(f"Text preprocessed, length: {len(text)}")
        return text
        
    except Exception as e:
        logger.error(f"Error preprocessing text: {str(e)}")
        return ""

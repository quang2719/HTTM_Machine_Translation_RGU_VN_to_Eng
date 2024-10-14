import csv

def create_data_csv(file_vi, file_eng, output_csv):
    # Đọc nội dung từ file tiếng Việt
    with open(file_vi, 'r', encoding='utf-8') as f_vi:
        data_vi = f_vi.read()
    
    # Đọc nội dung từ file tiếng Anh
    with open(file_eng, 'r', encoding='utf-8') as f_eng:
        data_eng = f_eng.read()
    
    # Tách các câu theo dấu chấm
    sentences_vi = data_vi.split('.')
    sentences_eng = data_eng.split('.')
    
    # Loại bỏ các khoảng trắng thừa ở đầu và cuối câu
    sentences_vi = [sentence.strip() for sentence in sentences_vi if sentence.strip()]
    sentences_eng = [sentence.strip() for sentence in sentences_eng if sentence.strip()]
    
    # Đảm bảo số lượng câu trong hai file là bằng nhau
    if len(sentences_vi) != len(sentences_eng):
        raise ValueError(
            f"Số lượng câu trong hai file không khớp.\n Vi: {len(sentences_vi)}, Eng: {len(sentences_eng)}"
            )
    
    # Tạo file CSV và ghi dữ liệu
    with open(output_csv, 'w', newline='', encoding='utf-8') as csvfile:
        csvwriter = csv.writer(csvfile)
        
        # Ghi tiêu đề
        csvwriter.writerow(['english', 'vietnamese'])
        
        # Ghi các câu tương ứng
        for eng_sentence, vi_sentence in zip(sentences_eng, sentences_vi):
            csvwriter.writerow([eng_sentence, vi_sentence])

# Sử dụng hàm để tạo file CSV
create_data_csv('data_vi.txt', 'data_eng.txt', 'output.csv')


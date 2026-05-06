# LaTeX Report Template

Template này được tối ưu cho sinh viên kỹ thuật, đặc biệt phù hợp với các báo cáo lab.

## Cấu trúc thư mục

```text
.
|-- assets/
|   `-- images/
|-- config/
|   |-- metadata.tex
|   |-- packages.tex
|   `-- settings.tex
|-- frontmatter/
|   `-- cover.tex
|-- sections/
|   |-- 01-overview.tex
|   |-- 02-objectives.tex
|   |-- 03-theory.tex
|   |-- 04-setup.tex
|   |-- 05-results.tex
|   |-- 06-discussion.tex
|   |-- 07-conclusion.tex
|   `-- 08-references.tex
`-- main.tex
```

## Cách dùng

1. Chọn ngôn ngữ trong `config/metadata.tex` bằng `\englishfalse` (tiếng Việt) hoặc `\englishtrue` (tiếng Anh). Cờ này sẽ đổi đồng bộ tên trường/khoa, `\tableofcontents`, tiêu đề chương/mục và một số caption mẫu.
2. Sửa thông tin sinh viên và tên bài lab trong `config/metadata.tex`.
3. Cập nhật nội dung từng mục trong thư mục `sections/`.
4. Đặt hình ảnh vào `assets/images/`.
5. Biên dịch bằng `pdflatex main.tex` hoặc `xelatex main.tex`.

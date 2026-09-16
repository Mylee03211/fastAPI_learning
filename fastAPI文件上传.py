# FastAPI 提供了 File 和 UploadFile 两种方式来处理文件上传，支持单独上传文件和表单与文件混合上传。、
from fastapi import FastAPI, UploadFile

app = FastAPI()


@app.post("/uploadfile/")
async def create_upload_file(file: UploadFile):
    # UploadFile 提供的属性和方法
    return {
        "filename": file.filename,          # 文件名
        "content_type": file.content_type,  # 文件 MIME 类型
        "size": file.size,                  # 文件大小（字节）
    }

# filename	str | None	上传文件的原始文件名
# content_type	str | None	文件的 MIME 类型（如 image/png）
# file	SpooledTemporaryFile	类似文件的对象，可读取文件内容
# size	int | None	文件大小（字节）
# read()	方法	读取文件内容为 bytes
# write()	方法	向文件写入内容
# seek()	方法	移动文件指针位置
# close()	方法	关闭文件

# uploadfile 很智能，会把小文件放在内存中，而大文件自动写入磁盘
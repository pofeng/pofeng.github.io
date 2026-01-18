#!/usr/bin/env python3
"""
Script to create an Open Office presentation (.odp) based on the weight management page from pofeng.org/w
"""

from odfdo import Document, DrawPage, Frame, Paragraph

def create_presentation():
    # Create a new presentation document
    doc = Document('presentation')

    # Get the body
    body = doc.body

    # Slide 1: Title
    slide1 = DrawPage("Title Slide")
    body.append(slide1)

    # Add title frame
    title_frame = Frame(size=("20cm", "5cm"), position=("3cm", "3cm"))
    title_para = Paragraph("李柏鋒診所 - 體重管理 (減重)")
    title_frame.append(title_para)
    slide1.append(title_frame)

    # Add subtitle frame
    subtitle_frame = Frame(size=("20cm", "3cm"), position=("3cm", "8cm"))
    subtitle_para = Paragraph("減重藥物與體重管理服務")
    subtitle_frame.append(subtitle_para)
    slide1.append(subtitle_frame)

    # Slide 2: Introduction
    slide2 = DrawPage("Introduction")
    body.append(slide2)

    intro_frame = Frame(size=("22cm", "15cm"), position=("1cm", "1cm"))
    intro_text = """初診請在 LINE 預約，諮詢費 650，可全額抵扣當次減重藥物費用

主要減重藥物：
• 猛健樂 (Mounjaro) - Tirzepatide
• 週纖達 (Wegovy) - Semaglutide
• 瑞倍適 (Rybelsus) - Semaglutide"""
    intro_para = Paragraph(intro_text)
    intro_frame.append(intro_para)
    slide2.append(intro_frame)

    # Slide 3: Common issues
    slide3 = DrawPage("Common Issues")
    body.append(slide3)

    issues_frame = Frame(size=("22cm", "15cm"), position=("1cm", "1cm"))
    issues_text = """體重過重，常見的暗藏問題：

• 血糖異常：檢驗血糖，糖化血色素 (HbA1c)，胰島素阻抗 (HOMA-IR)
• 甲狀腺素低下：TSH, freeT4
• 膽固醇，三酸甘油脂偏高
• 打呼 (呼吸中止症，OSA)
• 賀爾蒙異常 (多囊性卵巢症候群，PCOS)
• 胃酸過多：檢驗幽門桿菌"""
    issues_para = Paragraph(issues_text)
    issues_frame.append(issues_para)
    slide3.append(issues_frame)

    # Slide 4: Medications
    slide4 = DrawPage("Medications")
    body.append(slide4)

    meds_frame = Frame(size=("22cm", "15cm"), position=("1cm", "1cm"))
    meds_text = """減重藥物選擇：

💉 猛健樂 (Mounjaro, Tirzepatide)
💉 胰妥讚 週纖達 (Ozempic, Wegovy, Semaglutide)
💊 瑞倍適 (Rybelsus, Semaglutide)

其他輔助藥物：
• 易週糖 (Trulicity, Dulaglutide)
• 恩排糖
• 二甲雙胍 (Metformin)
• 優美孅 (Orlistat)
• 康纖芙 (Naltrexone + Bupropion)"""
    meds_para = Paragraph(meds_text)
    meds_frame.append(meds_para)
    slide4.append(meds_frame)

    # Slide 5: Diet
    slide5 = DrawPage("Diet")
    body.append(slide5)

    diet_frame = Frame(size=("22cm", "15cm"), position=("1cm", "1cm"))
    diet_text = """飲食注意事項：

🎯 目標一: 降低總熱量
• 不吃甜食(糖類)，降低澱粉(糖類)
• 少量優質澱粉: 糙米, 地瓜, 玉米, 蓮藕, 馬鈴薯
• 不吃精緻澱粉: 麵條, 麵包, 饅頭, 蛋糕, 薯條

🎯 目標二: 降低食慾
• 胃藥控制胃酸
• 減重藥控制食慾
• 選擇低 GI 食物
• 控制睡眠中止症候群"""
    diet_para = Paragraph(diet_text)
    diet_frame.append(diet_para)
    slide5.append(diet_frame)

    # Slide 6: Exercise
    slide6 = DrawPage("Exercise")
    body.append(slide6)

    exercise_frame = Frame(size=("22cm", "15cm"), position=("1cm", "1cm"))
    exercise_text = """💪🏼 阻力訓練

• 自由重量: 啞鈴、槓鈴、壺鈴
• 器械: 健身器材
• 自身體重: 伏地挺身、深蹲、引體向上
• 彈力帶: 提供阻力，適合不同強度"""
    exercise_para = Paragraph(exercise_text)
    exercise_frame.append(exercise_para)
    slide6.append(exercise_frame)

    # Slide 7: Contact
    slide7 = DrawPage("Contact")
    body.append(slide7)

    contact_frame = Frame(size=("22cm", "15cm"), position=("1cm", "1cm"))
    contact_text = """🏠 地址: (330) 桃園市桃園區中山路807號

🅿️ 停車資訊: /s/parking

📧 電郵: doc.pofeng.org@gmail.com

☎️ 電話: (03)220-7480, (03)220-8076

📱 LINE: /s/line

門診時間:
週一至週六 08:00~11:30, 15:00~21:00
週日 08:00~11:30"""
    contact_para = Paragraph(contact_text)
    contact_frame.append(contact_para)
    slide7.append(contact_frame)

    # Save the presentation
    doc.save("weight_management_presentation.odp")
    print("Presentation created: weight_management_presentation.odp")

if __name__ == "__main__":
    create_presentation()
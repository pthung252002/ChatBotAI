from rasa_sdk import Action
from rasa_sdk.events import SlotSet

class Action_CungCap_ThongTin_EB(Action):
    def name(self):
        return "EB_action_CungCap_ThongTin"

    def run(self, dispatcher, tracker, domain):
        disease = tracker.latest_message.get("text")
        dispatcher.utter_message(text=f"Bệnh {disease} (Early Blight) hay còn được gọi là bệnh đốm vòng là một bệnh phổ biến trên cây cà chua do nấm Alternaria solani gây ra. Bệnh này thường xuất hiện trong điều kiện thời tiết ấm áp, độ ẩm cao và có thể ảnh hưởng nghiêm trọng đến năng suất cây trồng.")
        return [SlotSet("current_topic", disease)]
		

class Action_CungCap_NguyenNhan_EB(Action):
    def name(self):
        return "EB_action_CungCap_NguyenNhan"

    def run(self, dispatcher, tracker, domain):
        current_topic = tracker.get_slot("current_topic")
        disease = tracker.latest_message.get("text")  # Lấy tên bệnh từ câu hỏi
        
        if not current_topic and disease:  
            current_topic = disease
            
        if current_topic:
            dispatcher.utter_message(text=f"Nguyên nhân của {current_topic} là do nấm Alternaria solani gây ra. Đây là loại nấm phổ biến, tồn tại trong tàn dư cây trồng, đất và lây lan qua gió, nước hoặc dụng cụ làm vườn.")
            return [SlotSet("current_topic", current_topic)]  # Cập nhật slot
        else:
            dispatcher.utter_message(response="utter_Hoi_NguyenNhan")
            return []


class Action_CungCap_TrieuChung_EB(Action):
    def name(self):
        return "EB_action_CungCap_TrieuChung"

    def run(self, dispatcher, tracker, domain):
        current_topic = tracker.get_slot("current_topic")
        disease = tracker.latest_message.get("text")  # Lấy tên bệnh từ câu hỏi
                
        if not current_topic and disease:  
            current_topic = disease
            
        if current_topic:
            dispatcher.utter_message(text=f"Triệu chứng của {current_topic}như sau:/n - Trên lá: Xuất hiện các đốm tròn màu nâu sẫm, có viền vàng xung quanh, kích thước từ 3-10 mm. Khi bệnh phát triển, các đốm có dạng vòng đồng tâm như vân gỗ. Lá bị nhiễm bệnh nặng sẽ vàng và rụng sớm./n - Trên thân cây con: Xuất hiện vết lõm màu nâu đen, có thể gây chết cây non./n - Trên quả: Đốm bệnh xuất hiện ở phần gần cuống, màu nâu sẫm, lõm xuống, có thể lan rộng và làm quả thối rụng.")
            return [SlotSet("current_topic", current_topic)]  # Cập nhật slot
        else:
            dispatcher.utter_message(response="utter_Hoi_TrieuChung")
            return []


class Action_CungCap_PhongNgua_EB(Action):
    def name(self):
        return "EB_action_CungCap_PhongNgua"

    def run(self, dispatcher, tracker, domain):
        current_topic = tracker.get_slot("current_topic")
        disease = tracker.latest_message.get("text")  # Lấy tên bệnh từ câu hỏi
        
        if not current_topic and disease:  
            current_topic = disease
                    
        if current_topic:
            dispatcher.utter_message(text=f"Cách phòng ngừa {current_topic}:/n - Luân canh cây trồng, tránh trồng cà chua liên tục nhiều vụ trên cùng một đất./n - Vệ sinh đồng ruộng, tiêu hủy cây bệnh, làm đất kỹ trước khi trồng./n - Trồng cây với khoảng cách hợp lý để tạo sự thông thoáng.")
            return [SlotSet("current_topic", current_topic)]  # Cập nhật slot
        else:
            dispatcher.utter_message(response="utter_Hoi_PhongNgua")
            return []
        

# ========== LB ==========
class Action_CungCap_ThongTin_LB(Action):
    def name(self):
        return "LB_action_CungCap_ThongTin"

    def run(self, dispatcher, tracker, domain):
        disease = tracker.latest_message.get("text")
        dispatcher.utter_message(text=f"Bệnh {disease} (Late Blight) là một trong những bệnh nguy hiểm nhất trên cây cà chua, do tác nhân Phytophthora infestans (một loại nấm nước) gây ra. Bệnh có khả năng lây lan nhanh trong điều kiện mưa ẩm, gây thất thu lớn trong sản xuất cà chua.")
        return [SlotSet("current_topic", disease)]
		

class Action_CungCap_NguyenNhan_LB(Action):
    def name(self):
        return "LB_action_CungCap_NguyenNhan"

    def run(self, dispatcher, tracker, domain):
        current_topic = tracker.get_slot("current_topic")
        disease = tracker.latest_message.get("text")  # Lấy tên bệnh từ câu hỏi
        
        if not current_topic and disease:  
            current_topic = disease
 
        if current_topic:
            dispatcher.utter_message(text=f"Nguyên nhân của {current_topic} là do tác nhân Phytophthora infestans gây ra. Đây là một loại nấm nước có khả năng phát triển và lây lan nhanh chóng trong điều kiện ẩm ướt, mát mẻ, gây hại nghiêm trọng đến lá, thân và quả cà chua.")
            return [SlotSet("current_topic", current_topic)]  # Cập nhật slot
        else:
            dispatcher.utter_message(response="utter_Hoi_NguyenNhan")
            return []


class Action_CungCap_TrieuChung_LB(Action):
    def name(self):
        return "LB_action_CungCap_TrieuChung"

    def run(self, dispatcher, tracker, domain):
        current_topic = tracker.get_slot("current_topic")
        disease = tracker.latest_message.get("text")  # Lấy tên bệnh từ câu hỏi
        
        if not current_topic and disease:  
            current_topic = disease
            
        if current_topic:
            dispatcher.utter_message(text=f"Triệu chứng của {current_topic}như sau:/n - Trên lá: Xuất hiện các đốm xanh xám, sau đó lan rộng thành màu nâu sẫm với quầng vàng xung quanh. Trong điều kiện ẩm ướt, mặt dưới lá có lớp mốc trắng chứa bào tử nấm./n - Trên thân và cành: Các vết bệnh thâm đen, kéo dài dọc theo thân, làm cây héo rũ và chết nhanh chóng./n - Trên quả: Các đốm bệnh màu nâu cứng, hơi lõm xuống, có thể lan rộng và gây thối toàn bộ quả.")
            return [SlotSet("current_topic", current_topic)]  # Cập nhật slot        
        else:
            dispatcher.utter_message(response="utter_Hoi_TrieuChung")
            return []


class Action_CungCap_PhongNgua_LB(Action):
    def name(self):
        return "LB_action_CungCap_PhongNgua"

    def run(self, dispatcher, tracker, domain):
        current_topic = tracker.get_slot("current_topic")
        disease = tracker.latest_message.get("text")  # Lấy tên bệnh từ câu hỏi
        
        if not current_topic and disease:  
            current_topic = disease
            
        if current_topic:
            dispatcher.utter_message(text=f"Cách phòng ngừa {current_topic}:/n - Luân canh cây trồng với các loại cây khác ngoài họ cà./n - Trồng cây thông thoáng, mật độ hợp lý để giảm độ ẩm./n - Tưới nước vào gốc, tránh tưới lên lá vào buổi chiều tối.")
            return [SlotSet("current_topic", current_topic)]  # Cập nhật slot
        else:
            dispatcher.utter_message(response="utter_Hoi_PhongNgua")
            return []
        
        
# ========== LM ==========
class Action_CungCap_ThongTin_LM(Action):
    def name(self):
        return "LM_action_CungCap_ThongTin"

    def run(self, dispatcher, tracker, domain):
        disease = tracker.latest_message.get("text")
        dispatcher.utter_message(text=f"Bệnh {disease} (Leaf Miner) trên cây cà chua là ấu trùng của một số loài ruồi thuộc họ Agromyzidae, phổ biến nhất là Liriomyza spp.. Ấu trùng của loài này sống bên trong mô lá, ăn phần mô xanh và tạo thành các đường hầm ngoằn ngoèo, làm giảm khả năng quang hợp và ảnh hưởng đến sự sinh trưởng của cây.")
        return [SlotSet("current_topic", disease)]
		

class Action_CungCap_NguyenNhan_LM(Action):
    def name(self):
        return "LM_action_CungCap_NguyenNhan"

    def run(self, dispatcher, tracker, domain):
        current_topic = tracker.get_slot("current_topic")
        disease = tracker.latest_message.get("text")  # Lấy tên bệnh từ câu hỏi
        
        if not current_topic and disease:  
            current_topic = disease
            
        if current_topic:
            dispatcher.utter_message(text=f"Nguyên nhân của {current_topic} là do ấu trùng của các loài ruồi thuộc họ Agromyzidae, phổ biến nhất là Liriomyza spp.. Chúng gây hại trên cây cà chua bằng cách ăn mô lá, tạo các đường hầm ngoằn ngoèo màu trắng, làm giảm khả năng quang hợp và ảnh hưởng đến sự phát triển của cây.")
            return [SlotSet("current_topic", current_topic)]  # Cập nhật slot
        else:
            dispatcher.utter_message(response="utter_Hoi_NguyenNhan")
            return []


class Action_CungCap_TrieuChung_LM(Action):
    def name(self):
        return "LM_action_CungCap_TrieuChung"

    def run(self, dispatcher, tracker, domain):
        current_topic = tracker.get_slot("current_topic")
        disease = tracker.latest_message.get("text")  # Lấy tên bệnh từ câu hỏi
        
        if not current_topic and disease:  
            current_topic = disease
            
        if current_topic:
            dispatcher.utter_message(text=f"Triệu chứng của {current_topic}như sau:/n - Trên lá: Xuất hiện các đường hầm màu trắng bạc chạy ngoằn ngoèo do ấu trùng ăn phần mô bên trong lá. Khi bị nặng, lá có thể khô héo và rụng./n - Trên cây non: Cây còi cọc, chậm phát triển do mất diện tích quang hợp./n - Ảnh hưởng đến năng suất: Lá bị hư hại nghiêm trọng có thể làm giảm sản lượng và chất lượng quả cà chua.")
            return [SlotSet("current_topic", current_topic)]  # Cập nhật slot
        else:
            dispatcher.utter_message(response="utter_Hoi_TrieuChung")
            return []


class Action_CungCap_PhongNgua_LM(Action):
    def name(self):
        return "LM_action_CungCap_PhongNgua"

    def run(self, dispatcher, tracker, domain):
        current_topic = tracker.get_slot("current_topic")
        disease = tracker.latest_message.get("text")  # Lấy tên bệnh từ câu hỏi
        if not current_topic and disease: 
            current_topic = disease
            
        if current_topic:
            dispatcher.utter_message(text=f"Cách phòng ngừa {current_topic}:/n - Luân canh cây trồng để giảm sự tích lũy sâu bệnh./n - Dọn sạch tàn dư cây trồng, cắt bỏ lá bị hại để ngăn chặn sự phát triển của sâu./n - Tưới nước và bón phân hợp lý giúp cây khỏe mạnh, tăng sức đề kháng.")
            return [SlotSet("current_topic", current_topic)]  # Cập nhật slot
        else:
            dispatcher.utter_message(response="utter_Hoi_PhongNgua")
            return []
        
        
# ========== LMold ==========
class Action_CungCap_ThongTin_LMold(Action):
    def name(self):
        return "LMold_action_CungCap_ThongTin"

    def run(self, dispatcher, tracker, domain):
        disease = tracker.latest_message.get("text")
        dispatcher.utter_message(text=f"Bệnh {disease} (Leaf Mold) trên cây cà chua do nấm Passalora fulva (trước đây gọi là Cladosporium fulvum) gây ra. Đây là bệnh phổ biến trong điều kiện nhiệt độ ấm, độ ẩm cao, gây hại chủ yếu trên lá, làm giảm khả năng quang hợp và ảnh hưởng đến năng suất cây trồng.")
        return [SlotSet("current_topic", disease)]
		

class Action_CungCap_NguyenNhan_LMold(Action):
    def name(self):
        return "LMold_action_CungCap_NguyenNhan"

    def run(self, dispatcher, tracker, domain):
        current_topic = tracker.get_slot("current_topic")
        disease = tracker.latest_message.get("text")  # Lấy tên bệnh từ câu hỏi
        
        if not current_topic and disease:  
            current_topic = disease
            
        if current_topic:
            dispatcher.utter_message(text=f"Nguyên nhân của {current_topic} là do nấm Passalora fulva (trước đây gọi là Cladosporium fulvum) gây ra. Bệnh chủ yếu ảnh hưởng đến lá, làm giảm khả năng quang hợp và có thể gây rụng lá hàng loạt, ảnh hưởng đến năng suất cây trồng.")
            return [SlotSet("current_topic", current_topic)]  # Cập nhật slot
        else:
            dispatcher.utter_message(response="utter_Hoi_NguyenNhan")
            return []


class Action_CungCap_TrieuChung_LMold(Action):
    def name(self):
        return "LMold_action_CungCap_TrieuChung"

    def run(self, dispatcher, tracker, domain):
        current_topic = tracker.get_slot("current_topic")
        disease = tracker.latest_message.get("text")  # Lấy tên bệnh từ câu hỏi
        
        if not current_topic and disease:
            current_topic = disease
            
        if current_topic:
            dispatcher.utter_message(text=f"Triệu chứng của {current_topic}như sau:/n - Giai đoạn đầu: Xuất hiện các đốm vàng nhạt trên mặt trên của lá, thường bắt đầu từ lá già./n - Giai đoạn tiến triển: Mặt dưới lá có lớp mốc màu xanh ô liu hoặc nâu xám do bào tử nấm phát triển./n - Giai đoạn nặng: Lá bị bệnh khô héo, xoăn lại và rụng sớm, làm cây suy yếu và giảm năng suất.")
            return [SlotSet("current_topic", current_topic)]  # Cập nhật slot
        else:
            dispatcher.utter_message(response="utter_Hoi_TrieuChung")
            return []


class Action_CungCap_PhongNgua_LMold(Action):
    def name(self):
        return "LMold_action_CungCap_PhongNgua"

    def run(self, dispatcher, tracker, domain):
        current_topic = tracker.get_slot("current_topic")
        disease = tracker.latest_message.get("text")  # Lấy tên bệnh từ câu hỏi
        
        if not current_topic and disease:  
            current_topic = disease
            
        if current_topic:
            dispatcher.utter_message(text=f"Cách phòng ngừa {current_topic}:/n - Trồng cây với mật độ hợp lý, cắt tỉa lá già để tạo độ thông thoáng./n - Tưới nước vào gốc, tránh làm ướt lá, đặc biệt vào buổi chiều tối./n - Dọn sạch tàn dư cây trồng sau mỗi vụ để giảm nguồn lây bệnh.")
            return [SlotSet("current_topic", current_topic)]  # Cập nhật slot
        else:
            dispatcher.utter_message(response="utter_Hoi_PhongNgua")
            return []
        
   
# ========== MV ==========
class Action_CungCap_ThongTin_MV(Action):
    def name(self):
        return "MV_action_CungCap_ThongTin"

    def run(self, dispatcher, tracker, domain):
        disease = tracker.latest_message.get("text")
        dispatcher.utter_message(text=f"Bệnh {disease} (Mosaic Virus) trên cây cà chua là do virus gây ra, làm biến dạng lá, giảm khả năng quang hợp và làm giảm năng suất đáng kể.")
        return [SlotSet("current_topic", disease)]
		

class Action_CungCap_NguyenNhan_MV(Action):
    def name(self):
        return "MV_action_CungCap_NguyenNhan"

    def run(self, dispatcher, tracker, domain):
        current_topic = tracker.get_slot("current_topic")
        disease = tracker.latest_message.get("text")  # Lấy tên bệnh từ câu hỏi
        
        if not current_topic and disease: 
            current_topic = disease
            
        if current_topic:
            dispatcher.utter_message(text=f"Nguyên nhân của {current_topic} là do nhiều loại virus gây ra, phổ biến nhất là: Tobacco Mosaic Virus (TMV) – Virus khảm thuốc lá và Tomato Mosaic Virus (ToMV) – Virus khảm cà chua.")
            return [SlotSet("current_topic", current_topic)]  # Cập nhật slot
        else:
            dispatcher.utter_message(response="utter_Hoi_NguyenNhan")
            return []


class Action_CungCap_TrieuChung_MV(Action):
    def name(self):
        return "MV_action_CungCap_TrieuChung"

    def run(self, dispatcher, tracker, domain):
        current_topic = tracker.get_slot("current_topic")
        disease = tracker.latest_message.get("text")  # Lấy tên bệnh từ câu hỏi
        
        if not current_topic and disease:
            current_topic = disease
            
        if current_topic:
            dispatcher.utter_message(text=f"Triệu chứng của {current_topic}như sau:/n - Trên lá: Xuất hiện vệt loang lổ màu xanh đậm – xanh nhạt giống hoa văn khảm, lá bị nhăn nheo, cong queo, nhỏ hơn bình thường./n - Trên thân và cây: Cây còi cọc, chậm phát triển, có thể xuất hiện vết nứt trên thân hoặc cuống lá./n - Trên quả: Quả nhỏ, chín không đều, méo mó, đôi khi có đốm vàng hoặc nâu.")
            return [SlotSet("current_topic", current_topic)]  # Cập nhật slot
        else:
            dispatcher.utter_message(response="utter_Hoi_TrieuChung")
            return []


class Action_CungCap_PhongNgua_MV(Action):
    def name(self):
        return "MV_action_CungCap_PhongNgua"

    def run(self, dispatcher, tracker, domain):
        current_topic = tracker.get_slot("current_topic")
        disease = tracker.latest_message.get("text")  # Lấy tên bệnh từ câu hỏi
        
        if not current_topic and disease:  
            current_topic = disease
            
        if current_topic:
            dispatcher.utter_message(text=f"Cách phòng ngừa {current_topic}:/n - Luân canh cây trồng với cây không phải ký chủ của virus (lúa, ngô, đậu)./n - Sử dụng hạt giống sạch, không mang mầm bệnh./n - Dọn sạch tàn dư cây trồng sau mỗi vụ để loại bỏ nguồn bệnh.")
            return [SlotSet("current_topic", current_topic)]  # Cập nhật slot
        else:
            dispatcher.utter_message(response="utter_Hoi_PhongNgua")
            return []
        
      
# ========== Sep ==========
class Action_CungCap_ThongTin_Sep(Action):
    def name(self):
        return "Sep_action_CungCap_ThongTin"

    def run(self, dispatcher, tracker, domain):
        disease = tracker.latest_message.get("text")
        dispatcher.utter_message(text=f"Bệnh {disease} là một trong những bệnh phổ biến làm rụng lá sớm, khiến cây suy yếu và ảnh hưởng đến năng suất.")
        return [SlotSet("current_topic", disease)]
		

class Action_CungCap_NguyenNhan_Sep(Action):
    def name(self):
        return "Sep_action_CungCap_NguyenNhan"

    def run(self, dispatcher, tracker, domain):
        current_topic = tracker.get_slot("current_topic")
        disease = tracker.latest_message.get("text")  # Lấy tên bệnh từ câu hỏi
        
        if not current_topic and disease:  
            current_topic = disease
            
        if current_topic:
            dispatcher.utter_message(text=f"Nguyên nhân của {current_topic} là do nấm Septoria lycopersici gây ra")
            return [SlotSet("current_topic", current_topic)]  # Cập nhật slot
        else:
            dispatcher.utter_message(response="utter_Hoi_NguyenNhan")
            return []


class Action_CungCap_TrieuChung_Sep(Action):
    def name(self):
        return "Sep_action_CungCap_TrieuChung"

    def run(self, dispatcher, tracker, domain):
        current_topic = tracker.get_slot("current_topic")
        disease = tracker.latest_message.get("text")  # Lấy tên bệnh từ câu hỏi
        
        if not current_topic and disease:
            current_topic = disease
            
        if current_topic:
            dispatcher.utter_message(text=f"Triệu chứng của {current_topic}như sau:/n - Giai đoạn đầu: Xuất hiện những đốm nhỏ, tròn, màu nâu hoặc xám với viền đậm trên lá già ở phần dưới của cây./n - Giai đoạn tiến triển: Đốm bệnh mở rộng, có đường kính khoảng 1-3mm, trung tâm có màu xám nhạt hoặc trắng, viền ngoài màu nâu sẫm, xuất hiện các chấm đen nhỏ li ti trong vùng trung tâm (đây là bào tử nấm)./n - Giai đoạn nặng: Các lá bệnh vàng úa, khô và rụng sớm, khiến cây bị mất khả năng quang hợp, bệnh có thể lan lên thân và cuống lá, nhưng hiếm khi ảnh hưởng đến quả.")
            return [SlotSet("current_topic", current_topic)]  # Cập nhật slot
        else:
            dispatcher.utter_message(response="utter_Hoi_TrieuChung")
            return []


class Action_CungCap_PhongNgua_Sep(Action):
    def name(self):
        return "Sep_action_CungCap_PhongNgua"

    def run(self, dispatcher, tracker, domain):
        current_topic = tracker.get_slot("current_topic")
        disease = tracker.latest_message.get("text")  # Lấy tên bệnh từ câu hỏi
        
        if not current_topic and disease:  
            current_topic = disease
            
        if current_topic:
            dispatcher.utter_message(text=f"Cách phòng ngừa {current_topic}:/n - Cắt tỉa lá già, lá bệnh để vườn thông thoáng, giảm độ ẩm./n - Tưới nước vào gốc, không tưới lên lá để hạn chế lây lan bào tử nấm./n - Luân canh cây trồng với cây không thuộc họ cà để giảm nguồn bệnh trong đất.")
            return [SlotSet("current_topic", current_topic)]  # Cập nhật slot
        else:
            dispatcher.utter_message(response="utter_Hoi_PhongNgua")
            return []
        
        
# ========== SM ==========
class Action_CungCap_ThongTin_SM(Action):
    def name(self):
        return "SM_action_CungCap_ThongTin"

    def run(self, dispatcher, tracker, domain):
        disease = tracker.latest_message.get("text")
        dispatcher.utter_message(text=f"Bệnh {disease}: Nhện đỏ (Tên khoa học: Tetranychus urticae và Tetranychus evansi) là loài gây hại phổ biến trên cà chua. Chúng chích hút dịch lá, làm cây suy yếu, giảm năng suất và có thể gây chết cây nếu không kiểm soát kịp thời.")
        return [SlotSet("current_topic", disease)]
		

class Action_CungCap_NguyenNhan_SM(Action):
    def name(self):
        return "SM_action_CungCap_NguyenNhan"

    def run(self, dispatcher, tracker, domain):
        current_topic = tracker.get_slot("current_topic")
        disease = tracker.latest_message.get("text")  # Lấy tên bệnh từ câu hỏi
        
		if not current_topic and disease:  
			current_topic = disease
            
        if current_topic:
            dispatcher.utter_message(text=f"Nguyên nhân của {current_topic} là do Nhện đỏ (Tetranychus urticae và Tetranychus evansi) gây ra. Chúng chích hút dịch lá, làm cây suy yếu, giảm năng suất và có thể gây chết cây nếu không kiểm soát kịp thời. Nhện đỏ sinh sản rất nhanh trong điều kiện khô nóng, dễ bùng phát thành dịch.")
            return [SlotSet("current_topic", current_topic)]  # Cập nhật slot
        else:
            dispatcher.utter_message(response="utter_Hoi_NguyenNhan")
            return []


class Action_CungCap_TrieuChung_SM(Action):
    def name(self):
        return "SM_action_CungCap_TrieuChung"

    def run(self, dispatcher, tracker, domain):
        current_topic = tracker.get_slot("current_topic")
        disease = tracker.latest_message.get("text")  # Lấy tên bệnh từ câu hỏi
        
		if not current_topic and disease:  
			current_topic = disease
            
        if current_topic:
            dispatcher.utter_message(text=f"Triệu chứng của {current_topic}như sau:/n - Giai đoạn đầu: Xuất hiện các chấm nhỏ màu vàng hoặc bạc trên mặt trên của lá, lá có vẻ mất màu, xỉn hơn bình thường./n - Giai đoạn tiến triển: Lá bị vàng úa, khô héo và có thể rụng sớm, xuất hiện mạng tơ mỏng do nhện đỏ giăng trên lá, thân và đọt cây./n - Giai đoạn nặng: Lá khô cháy, giòn và biến dạng.")
        	return [SlotSet("current_topic", current_topic)]  # Cập nhật slot
        else:
            dispatcher.utter_message(response="utter_Hoi_TrieuChung")
            return []


class Action_CungCap_PhongNgua_SM(Action):
    def name(self):
        return "SM_action_CungCap_PhongNgua"

    def run(self, dispatcher, tracker, domain):
        current_topic = tracker.get_slot("current_topic")
        disease = tracker.latest_message.get("text")  # Lấy tên bệnh từ câu hỏi
        
		if not current_topic and disease:  
			current_topic = disease
            
        if current_topic:
            dispatcher.utter_message(text=f"Cách phòng ngừa {current_topic}:/n - Tưới nước hợp lý: Nhện đỏ không thích ẩm, nên có thể tăng độ ẩm vườn bằng cách tưới phun sương nhẹ./n - Cắt tỉa lá già, lá bệnh, giúp vườn thông thoáng, giảm nơi trú ẩn của nhện đỏ./n - Luân canh cây trồng để hạn chế tích tụ nhện đỏ từ vụ trước.")
        	return [SlotSet("current_topic", current_topic)]  # Cập nhật slot
        else:
            dispatcher.utter_message(response="utter_Hoi_PhongNgua")
            return []
        
        
# ========== CV ==========
class Action_CungCap_ThongTin_CV(Action):
    def name(self):
        return "CV_action_CungCap_ThongTin"

    def run(self, dispatcher, tracker, domain):
        disease = tracker.latest_message.get("text")
        dispatcher.utter_message(text=f"Bệnh {disease} (Tomato Yellow Leaf Curl Virus) là một bệnh virus nguy hiểm trên cây cà chua, do bọ phấn trắng (Bemisia tabaci) truyền nhiễm. Bệnh gây biến dạng lá, còi cọc, giảm năng suất nghiêm trọng và không có thuốc đặc trị, chỉ có thể phòng ngừa và kiểm soát côn trùng truyền bệnh.")
        return [SlotSet("current_topic", disease)]
		

class Action_CungCap_NguyenNhan_CV(Action):
    def name(self):
        return "CV_action_CungCap_NguyenNhan"

    def run(self, dispatcher, tracker, domain):
        current_topic = tracker.get_slot("current_topic")
        disease = tracker.latest_message.get("text")  # Lấy tên bệnh từ câu hỏi
        
		if not current_topic and disease:  
			current_topic = disease
            
        if current_topic:
            dispatcher.utter_message(text=f"Nguyên nhân của {current_topic} gây ra bởi virus thuộc họ Geminiviridae. Virus này được bọ phấn trắng (Bemisia tabaci) truyền từ cây bệnh sang cây khỏe.")
        	return [SlotSet("current_topic", current_topic)]  # Cập nhật slot
        else:
            dispatcher.utter_message(response="utter_Hoi_NguyenNhan")
            return []


class Action_CungCap_TrieuChung_CV(Action):
    def name(self):
        return "CV_action_CungCap_TrieuChung"

    def run(self, dispatcher, tracker, domain):
        current_topic = tracker.get_slot("current_topic")
        disease = tracker.latest_message.get("text")  # Lấy tên bệnh từ câu hỏi
        
		if not current_topic and disease:  
			current_topic = disease
            
        if current_topic:
            dispatcher.utter_message(text=f"Triệu chứng của {current_topic}như sau:/n - Lá non bị xoăn, cong ngược lên trên, mép lá gợn sóng, có màu vàng nhạt./n - Cây sinh trưởng kém, thân còi cọc, ít ra cành nhánh./n - Hoa rụng sớm, ít đậu quả hoặc không có quả.")
        	return [SlotSet("current_topic", current_topic)]  # Cập nhật slot
        else:
            dispatcher.utter_message(response="utter_Hoi_TrieuChung")
            return []


class Action_CungCap_PhongNgua_CV(Action):
    def name(self):
        return "CV_action_CungCap_PhongNgua"

    def run(self, dispatcher, tracker, domain):
        current_topic = tracker.get_slot("current_topic")
        disease = tracker.latest_message.get("text")  # Lấy tên bệnh từ câu hỏi
        
		if not current_topic and disease:  
			current_topic = disease
            
        if current_topic:
            dispatcher.utter_message(text=f"Cách phòng ngừa {current_topic}:/n - Trồng xen cây xua đuổi bọ phấn như cúc vạn thọ, tỏi, húng quế./n - Dùng bẫy dính màu vàng để thu hút và tiêu diệt bọ phấn./n - Phun các chế phẩm sinh học như dầu neem, dịch tỏi, ớt để đuổi bọ phấn.")
        	return [SlotSet("current_topic", current_topic)]  # Cập nhật slot
        else:
            dispatcher.utter_message(response="utter_Hoi_PhongNgua")
            return []
"""
RPA数据采集模块
负责自动登录系统、抓取数据、OCR识别等功能
"""

class RPADataCollector:
    """
    RPA数据采集器
    模拟RPA机器人的数据抓取功能
    """
    
    def __init__(self, system_configs):
        """
        初始化RPA数据采集器
        :param system_configs: 系统配置信息
        """
        self.system_configs = system_configs
        self.collected_data = []
        
    def login_system(self, system_name):
        """
        模拟登录指定系统
        :param system_name: 系统名称
        :return: 登录状态
        """
        print(f"RPA机器人正在登录{system_name}系统...")
        # 模拟登录过程
        return True
    
    def collect_customer_data(self, customer_id):
        """
        收集客户数据
        :param customer_id: 客户ID
        :return: 收集的客户数据
        """
        print(f"RPA机器人正在抓取客户 {customer_id} 的数据...")
        
        # 模拟抓取不同类型的客户数据
        customer_data = {
            "customer_id": customer_id,
            "id_card": self._collect_id_card(customer_id),
            "income_proof": self._collect_income_proof(customer_id),
            "phone_info": self._collect_phone_info(customer_id),
            "history_records": self._collect_history_records(customer_id),
            "application_form": self._collect_application_form(customer_id)
        }
        
        self.collected_data.append(customer_data)
        return customer_data
    
    def _collect_id_card(self, customer_id):
        """收集身份证信息"""
        print("  - 收集身份证照片（正反面）")
        return {
            "front": f"id_card_front_{customer_id}.jpg",
            "back": f"id_card_back_{customer_id}.jpg"
        }
    
    def _collect_income_proof(self, customer_id):
        """收集收入证明"""
        print("  - 收集收入证明（PDF/图片）")
        return [f"income_proof_{customer_id}_1.pdf", f"income_proof_{customer_id}_2.jpg"]
    
    def _collect_phone_info(self, customer_id):
        """收集手机号实名信息"""
        print("  - 收集手机号实名信息")
        return {
            "phone_number": f"138****{customer_id[-4:]}",
            "real_name": f"客户{customer_id}",
            "operator": "中国移动",
            "real_name_verified": True
        }
    
    def _collect_history_records(self, customer_id):
        """收集历史保单记录"""
        print("  - 收集历史保单记录")
        return [
            {"policy_id": f"POL{customer_id}001", "status": "正常", "claim_history": []},
            {"policy_id": f"POL{customer_id}002", "status": "已结案", "claim_history": [{"date": "2024-01-15", "amount": 5000}]}
        ]
    
    def _collect_application_form(self, customer_id):
        """收集申请表单内容"""
        print("  - 收集申请表单内容")
        return {
            "product_type": "健康保险",
            "insurance_amount": 100000,
            "application_date": "2024-11-05",
            "health_questionnaire": {"has_chronic_disease": False, "has_surgery_history": False}
        }
    
    def ocr_recognize(self, image_path):
        """
        OCR识别功能
        :param image_path: 图片路径
        :return: 识别结果
        """
        print(f"正在对 {image_path} 进行OCR识别...")
        # 模拟OCR识别结果
        if "id_card" in image_path:
            return {
                "name": "张三",
                "id_number": "110101199001011234",
                "address": "北京市朝阳区xxx街道xxx号",
                "issue_date": "2020.01.01",
                "expiry_date": "2030.01.01"
            }
        else:
            return {"text": f"OCR识别结果来自{image_path}"}
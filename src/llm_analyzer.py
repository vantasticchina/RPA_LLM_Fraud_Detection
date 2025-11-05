"""
LLM智能分析模块
负责多模态理解、风险评分、审批建议等功能
"""

class LLMAnalyzer:
    """
    大语言模型分析器
    模拟LLM对多模态数据的理解与分析功能
    """
    
    def __init__(self, model_config):
        """
        初始化LLM分析器
        :param model_config: 模型配置
        """
        self.model_config = model_config
        
    def analyze_multimodal_data(self, data):
        """
        多模态数据分析
        :param data: 输入的多模态数据
        :return: 分析结果
        """
        print("LLM正在对多模态数据进行分析...")
        
        # 分析身份证信息
        id_analysis = self._analyze_id_card(data.get("id_card"))
        
        # 分析收入证明
        income_analysis = self._analyze_income_proof(data.get("income_proof"))
        
        # 分析申请表单
        form_analysis = self._analyze_application_form(data.get("application_form"))
        
        # 综合分析
        analysis_result = {
            "id_analysis": id_analysis,
            "income_analysis": income_analysis,
            "form_analysis": form_analysis,
            "overall_risk_score": self._calculate_overall_risk_score(id_analysis, income_analysis, form_analysis)
        }
        
        return analysis_result
    
    def _analyze_id_card(self, id_card_data):
        """分析身份证信息"""
        print("  - 分析身份证信息")
        # 这里可以添加更复杂的身份证分析逻辑
        return {
            "valid": True,
            "name_match": True,
            "age": 34,
            "region": "北京",
            "notes": "身份证信息正常"
        }
    
    def _analyze_income_proof(self, income_proof_data):
        """分析收入证明"""
        print("  - 分析收入证明")
        # 这里可以添加OCR后的收入证明分析逻辑
        return {
            "monthly_income": 15000,
            "verification_status": "已验证",
            "source_reliability": "高",
            "notes": "收入证明材料完整"
        }
    
    def _analyze_application_form(self, form_data):
        """分析申请表单"""
        print("  - 分析申请表单")
        # 分析申请表单中的信息
        return {
            "product_fit": "良好",
            "coverage_reasonable": True,
            "health_status": "良好",
            "notes": "申请信息完整无误"
        }
    
    def _calculate_overall_risk_score(self, id_analysis, income_analysis, form_analysis):
        """计算综合风险评分"""
        # 根据各项分析结果计算风险评分
        base_score = 0
        
        # 身份证分析对评分的影响
        if not id_analysis["valid"]:
            base_score += 30
        if not id_analysis["name_match"]:
            base_score += 20
            
        # 收入分析对评分的影响
        if income_analysis["source_reliability"] == "低":
            base_score += 25
        if income_analysis["verification_status"] != "已验证":
            base_score += 15
            
        # 申请表分析对评分的影响
        if not form_analysis["coverage_reasonable"]:
            base_score += 20
            
        # 风险评分范围：0-100，越低越好
        return min(100, base_score)
    
    def generate_approval_advice(self, analysis_result, customer_data):
        """
        生成审批建议
        :param analysis_result: 分析结果
        :param customer_data: 客户数据
        :return: 审批建议
        """
        risk_score = analysis_result["overall_risk_score"]
        
        if risk_score < 20:
            advice = "该客户风险较低，建议批准申请。"
        elif risk_score < 50:
            advice = "该客户存在中等风险，建议人工复核后决定。"
        else:
            advice = "该客户风险较高，建议拒绝申请。"
            
        # 添加具体建议
        details = []
        if analysis_result["id_analysis"]["notes"]:
            details.append(f"身份证验证：{analysis_result['id_analysis']['notes']}")
        if analysis_result["income_analysis"]["notes"]:
            details.append(f"收入验证：{analysis_result['income_analysis']['notes']}")
        if analysis_result["form_analysis"]["notes"]:
            details.append(f"申请信息：{analysis_result['form_analysis']['notes']}")
            
        advice += f"\n详细分析：{'；'.join(details)}"
        advice += f"\n风险评分：{risk_score}（越低越好）"
        
        return advice
    
    def detect_fraud_patterns(self, data):
        """
        检测欺诈模式
        :param data: 客户数据
        :return: 欺诈检测结果
        """
        print("LLM正在检测欺诈模式...")
        
        # 模拟欺诈检测逻辑
        fraud_indicators = []
        
        # 检查一些常见的欺诈指标
        if data.get("application_form", {}).get("insurance_amount", 0) > 1000000:
            fraud_indicators.append("保险金额异常高")
        
        # 检查历史记录
        history = data.get("history_records", [])
        if len(history) == 0:
            fraud_indicators.append("无历史保单记录")
        
        return {
            "is_fraud": len(fraud_indicators) > 0,
            "indicators": fraud_indicators,
            "confidence": len(fraud_indicators) / 10.0 if fraud_indicators else 0
        }
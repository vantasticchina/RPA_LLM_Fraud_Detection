"""
风控决策引擎
负责基于分析结果做出风控决策
"""

class RiskDecisionEngine:
    """
    风控决策引擎
    根据LLM分析结果和预设规则做出风控决策
    """
    
    def __init__(self, risk_thresholds=None):
        """
        初始化风控决策引擎
        :param risk_thresholds: 风险阈值配置
        """
        # 默认风险阈值
        self.risk_thresholds = risk_thresholds or {
            "low_risk": 20,
            "medium_risk": 50,
            "high_risk": 80
        }
    
    def make_decision(self, analysis_result, fraud_detection_result, customer_data):
        """
        基于分析结果做出风控决策
        :param analysis_result: LLM分析结果
        :param fraud_detection_result: 欺诈检测结果
        :param customer_data: 客户数据
        :return: 决策结果
        """
        print("风控决策引擎正在处理分析结果...")
        
        risk_score = analysis_result["overall_risk_score"]
        is_fraud = fraud_detection_result["is_fraud"]
        
        # 根据风险评分和欺诈检测结果做出决策
        if is_fraud:
            decision = "REJECT"
            reason = f"检测到欺诈行为: {', '.join(fraud_detection_result['indicators'])}"
        elif risk_score >= self.risk_thresholds["high_risk"]:
            decision = "REJECT"
            reason = f"风险评分过高({risk_score})，超过高风险阈值({self.risk_thresholds['high_risk']})"
        elif risk_score >= self.risk_thresholds["medium_risk"]:
            decision = "REVIEW"
            reason = f"中等风险({risk_score})，需要人工复核"
        else:
            decision = "APPROVE"
            reason = f"风险评分较低({risk_score})，符合准入标准"
        
        decision_result = {
            "decision": decision,
            "reason": reason,
            "risk_score": risk_score,
            "fraud_detected": is_fraud,
            "fraud_indicators": fraud_detection_result.get("indicators", []),
            "confidence": fraud_detection_result.get("confidence", 0)
        }
        
        print(f"  - 决策: {decision}, 原因: {reason}")
        return decision_result
    
    def generate_risk_report(self, analysis_result, decision_result, customer_data):
        """
        生成风险评估报告
        :param analysis_result: 分析结果
        :param decision_result: 决策结果
        :param customer_data: 客户数据
        :return: 风险报告
        """
        print("生成风险评估报告...")

        report = {
            "customer_id": customer_data.get("customer_id"),
            "risk_score": decision_result["risk_score"],
            "decision": decision_result["decision"],
            "decision_reason": decision_result["reason"],
            "detailed_analysis": analysis_result,
            "fraud_indicators": decision_result["fraud_indicators"],
            "timestamp": __import__('datetime').datetime.now().isoformat()
        }

        return report
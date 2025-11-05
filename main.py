"""
RPA + LLM 智能风控系统 - 主入口函数（增强版）

该系统演示了如何结合RPA（机器人流程自动化）和大语言模型
构建智能风控闭环系统，实现从\"被动防御\"到\"主动预测\"的跃迁。
"""

import sys
import os

# 添加src目录到Python路径
sys.path.append(os.path.join(os.path.dirname(__file__), 'src'))

from src.fraud_detection_system import IntelligentFraudDetectionSystem


def main():
    """
    主函数 - 演示RPA+LLM智能风控系统
    """
    print("="*60)
    print("RPA + LLM 智能风控系统演示")
    print("实现从'被动防御'到'主动预测'的跃迁")
    print("="*60)
    
    # 系统配置
    system_configs = {
        "crm_system": {"url": "https://crm.example.com", "credentials": {"user": "rpa_user", "password": "rpa_pass"}},
        "bank_system": {"url": "https://bank-api.example.com", "api_key": "bank_api_key"},
        "credit_system": {"url": "https://credit.example.com", "token": "credit_token"}
    }
    
    # 模型配置
    model_configs = {
        "model_name": "gpt-4-vision",  # 支持多模态分析
        "api_key": "your-openai-api-key",  # 实际使用时需要配置真实API密钥
        "temperature": 0.1,  # 降低随机性，提高分析准确性
        "max_tokens": 2000
    }
    
    # 风险阈值配置
    risk_thresholds = {
        "low_risk": 20,
        "medium_risk": 50,
        "high_risk": 80
    }
    
    # 创建智能风控系统实例
    print("初始化智能风控系统...")
    fraud_system = IntelligentFraudDetectionSystem(
        system_configs=system_configs,
        model_configs=model_configs,
        risk_thresholds=risk_thresholds
    )
    
    # 模拟处理几个客户申请 - 包含不同风险等级
    print("\n开始模拟处理客户申请...")
    
    # 示例客户ID列表 - 包含不同风险等级
    customer_ids = [
        "CUST001",  # 低风险客户
        "CUST002",  # 中等风险客户
        "CUST003"   # 高风险/欺诈客户
    ]
    
    # 批量处理客户申请
    results = fraud_system.batch_process_applications(customer_ids)
    
    # 输出系统指标
    print("\n" + "="*60)
    print("系统处理指标统计:")
    metrics = fraud_system.get_system_metrics()
    print(f"总处理数: {metrics['total_processed']}")
    print(f"批准数量: {metrics['approved']} (批准率: {metrics['approval_rate']:.2%})")
    print(f"拒绝数量: {metrics['rejected']} (拒绝率: {metrics['rejection_rate']:.2%})")
    print(f"待复核数量: {metrics['under_review']}")
    
    print("\n" + "="*60)
    print("处理完成！系统日志中记录了所有处理详情。")
    
    # 演示特殊场景：欺诈检测
    print("\n" + "="*60)
    print("欺诈检测场景演示:")
    
    # 创建一个高风险客户（保险金额异常高）
    high_risk_customer_id = "CUST999"
    print(f"\n处理高风险客户 {high_risk_customer_id} (保险金额异常高)...")
    
    # 模拟创建一个有欺诈特征的客户数据
    high_risk_customer_data = {
        "customer_id": high_risk_customer_id,
        "id_card": fraud_system.rpa_collector._collect_id_card(high_risk_customer_id),
        "income_proof": fraud_system.rpa_collector._collect_income_proof(high_risk_customer_id),
        "phone_info": fraud_system.rpa_collector._collect_phone_info(high_risk_customer_id),
        "history_records": [],  # 没有历史记录 - 可能是欺诈指标
        "application_form": {
            "product_type": "健康保险",
            "insurance_amount": 2000000,  # 异常高的保险金额
            "application_date": "2024-11-05",
            "health_questionnaire": {"has_chronic_disease": False, "has_surgery_history": False}
        }
    }
    
    # 手动运行分析流程
    print("\n=== 步骤1-3: RPA数据采集 + LLM分析 + 欺诈检测 ===")
    analysis_result = fraud_system.llm_analyzer.analyze_multimodal_data(high_risk_customer_data)
    fraud_result = fraud_system.llm_analyzer.detect_fraud_patterns(high_risk_customer_data)
    
    print(f"\n欺诈检测结果: {fraud_result}")
    
    # 风控决策
    print("\n=== 步骤4: 风控决策 ===")
    decision_result = fraud_system.risk_engine.make_decision(analysis_result, fraud_result, high_risk_customer_data)
    print(f"决策结果: {decision_result}")
    
    # 生成审批建议
    print(f"\n=== 步骤5: 生成审批建议 ===")
    approval_advice = fraud_system.llm_analyzer.generate_approval_advice(analysis_result, high_risk_customer_data)
    print(f"审批建议: {approval_advice}")
    
    # 执行流程
    print(f"\n=== 步骤6: 执行后续流程 ===")
    execution_result = fraud_system.process_executor.execute_process(decision_result, high_risk_customer_data, approval_advice)
    print(f"执行结果: {execution_result}")
    
    print("\n" + "="*60)
    print("RPA + LLM 智能风控系统演示结束")
    print("此系统能够:")
    print("- 7x24小时不间断采集数据")
    print("- 对非结构化数据进行多模态理解")
    print("- 生成风险评分和审批建议")
    print("- 自动执行后续流程")
    print("- 反馈结果持续优化模型")
    print("="*60)


if __name__ == "__main__":
    main()
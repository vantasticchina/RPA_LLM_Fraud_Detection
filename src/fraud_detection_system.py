"""
主风控系统类
整合RPA、LLM分析、风控决策和流程执行模块
"""

from .rpa_collector import RPADataCollector
from .llm_analyzer import LLMAnalyzer
from .risk_decision_engine import RiskDecisionEngine
from .process_executor import ProcessExecutor


class IntelligentFraudDetectionSystem:
    """
    智能风控检测系统
    整合RPA数据采集、LLM分析、风控决策和流程执行功能
    """
    
    def __init__(self, system_configs, model_configs, risk_thresholds=None):
        """
        初始化智能风控系统
        :param system_configs: 系统配置
        :param model_configs: 模型配置
        :param risk_thresholds: 风险阈值配置
        """
        self.rpa_collector = RPADataCollector(system_configs)
        self.llm_analyzer = LLMAnalyzer(model_configs)
        self.risk_engine = RiskDecisionEngine(risk_thresholds)
        self.process_executor = ProcessExecutor()
        
        # 存储系统运行日志
        self.system_log = []
        
    def process_customer_application(self, customer_id):
        """
        处理客户申请全流程
        :param customer_id: 客户ID
        :return: 处理结果
        """
        print(f"开始处理客户 {customer_id} 的申请...")
        
        # 1. RPA数据采集
        print("\\n=== 步骤1: RPA数据采集 ===")
        customer_data = self.rpa_collector.collect_customer_data(customer_id)
        
        # 2. LLM智能分析
        print("\\n=== 步骤2: LLM智能分析 ===")
        analysis_result = self.llm_analyzer.analyze_multimodal_data(customer_data)
        
        # 3. 欺诈检测
        print("\\n=== 步骤3: 欺诈检测 ===")
        fraud_result = self.llm_analyzer.detect_fraud_patterns(customer_data)
        
        # 4. 风控决策
        print("\\n=== 步骤4: 风控决策 ===")
        decision_result = self.risk_engine.make_decision(analysis_result, fraud_result, customer_data)
        
        # 5. 生成审批建议
        print("\\n=== 步骤5: 生成审批建议 ===")
        approval_advice = self.llm_analyzer.generate_approval_advice(analysis_result, customer_data)
        print(f"审批建议: {approval_advice}")
        
        # 6. 执行后续流程
        print("\\n=== 步骤6: 执行后续流程 ===")
        execution_result = self.process_executor.execute_process(decision_result, customer_data, approval_advice)
        
        # 7. 反馈结果到平台
        print("\\n=== 步骤7: 反馈结果 ===")
        feedback_result = self.process_executor.feedback_to_model(execution_result, customer_data)
        
        # 记录到系统日志
        process_record = {
            "customer_id": customer_id,
            "customer_data": customer_data,
            "analysis_result": analysis_result,
            "fraud_result": fraud_result,
            "decision_result": decision_result,
            "approval_advice": approval_advice,
            "execution_result": execution_result,
            "feedback_result": feedback_result,
            "completed_at": __import__('datetime').datetime.now().isoformat()
        }
        self.system_log.append(process_record)
        
        print(f"\\n客户 {customer_id} 的申请处理完成。")
        print(f"最终决策: {decision_result['decision']}")
        
        return process_record
    
    def batch_process_applications(self, customer_ids):
        """
        批量处理客户申请
        :param customer_ids: 客户ID列表
        :return: 批量处理结果
        """
        print(f"开始批量处理 {len(customer_ids)} 个客户申请...")
        results = []
        
        for customer_id in customer_ids:
            result = self.process_customer_application(customer_id)
            results.append(result)
            
            # 打印分隔符
            print("\\n" + "="*60 + "\\n")
        
        return results
    
    def get_system_metrics(self):
        """
        获取系统运行指标
        :return: 系统指标
        """
        total_processed = len(self.system_log)
        approved_count = sum(1 for record in self.system_log if record['decision_result']['decision'] == 'APPROVE')
        rejected_count = sum(1 for record in self.system_log if record['decision_result']['decision'] == 'REJECT')
        review_count = sum(1 for record in self.system_log if record['decision_result']['decision'] == 'REVIEW')
        
        metrics = {
            "total_processed": total_processed,
            "approved": approved_count,
            "rejected": rejected_count,
            "under_review": review_count,
            "approval_rate": approved_count / total_processed if total_processed > 0 else 0,
            "rejection_rate": rejected_count / total_processed if total_processed > 0 else 0
        }
        
        return metrics
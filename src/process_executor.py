"""
流程执行器
负责执行后续流程（标记、预警、通知、阻断等）
"""

class ProcessExecutor:
    """
    流程执行器
    根据风控决策执行相应的后续流程
    """
    
    def __init__(self):
        """初始化流程执行器"""
        self.execution_log = []
    
    def execute_process(self, decision_result, customer_data, approval_advice):
        """
        执行相应的流程
        :param decision_result: 决策结果
        :param customer_data: 客户数据
        :param approval_advice: 审批建议
        :return: 执行结果
        """
        decision = decision_result["decision"]
        customer_id = customer_data.get("customer_id")
        
        print(f"根据决策 {decision} 执行相应流程...")
        
        if decision == "APPROVE":
            result = self._approve_process(customer_id, approval_advice, customer_data)
        elif decision == "REVIEW":
            result = self._review_process(customer_id, approval_advice, customer_data)
        elif decision == "REJECT":
            result = self._reject_process(customer_id, decision_result, approval_advice, customer_data)
        else:
            result = {"status": "ERROR", "message": f"未知决策类型: {decision}"}
        
        # 记录执行日志
        execution_record = {
            "customer_id": customer_id,
            "decision": decision,
            "execution_result": result,
            "timestamp": __import__('datetime').datetime.now().isoformat()
        }
        self.execution_log.append(execution_record)
        
        return result
    
    def _approve_process(self, customer_id, approval_advice, customer_data):
        """批准流程"""
        print(f"  - 执行批准流程：为客户 {customer_id} 创建保单")
        # 这里可以集成实际的业务系统调用
        actions = [
            f"创建保单客户 {customer_id}",
            "发送保单确认邮件",
            "更新客户状态为已批准"
        ]
        
        for action in actions:
            print(f"    - {action}")
        
        return {
            "status": "SUCCESS",
            "actions": actions,
            "advice": approval_advice
        }
    
    def _review_process(self, customer_id, approval_advice, customer_data):
        """复核流程"""
        print(f"  - 执行复核流程：将客户 {customer_id} 标记为待复核")
        actions = [
            f"标记客户 {customer_id} 为待复核状态",
            "发送复核通知给风控专员",
            "生成复核任务工单"
        ]
        
        for action in actions:
            print(f"    - {action}")
        
        # 通知相关方
        self._send_notification(customer_id, "需要人工复核", "risk_review")
        
        return {
            "status": "PENDING_REVIEW",
            "actions": actions,
            "advice": approval_advice
        }
    
    def _reject_process(self, customer_id, decision_result, approval_advice, customer_data):
        """拒绝流程"""
        print(f"  - 执行拒绝流程：拒绝客户 {customer_id} 的申请")
        
        actions = [
            f"拒绝客户 {customer_id} 的申请",
            f"记录拒绝原因: {decision_result['reason']}",
            "发送拒绝通知邮件"
        ]
        
        for action in actions:
            print(f"    - {action}")
        
        # 如果检测到欺诈，执行额外的安全措施
        if decision_result.get("fraud_detected"):
            fraud_actions = [
                f"将客户 {customer_id} 加入黑名单",
                "记录欺诈证据链",
                "发送安全警报"
            ]
            for action in fraud_actions:
                print(f"    - 欺诈相关操作: {action}")
        
        # 通知相关方
        notification_type = "fraud_alert" if decision_result.get("fraud_detected") else "rejection"
        self._send_notification(customer_id, decision_result['reason'], notification_type)
        
        return {
            "status": "REJECTED",
            "actions": actions,
            "fraud_detected": decision_result.get("fraud_detected"),
            "fraud_indicators": decision_result.get("fraud_indicators", []),
            "advice": approval_advice
        }
    
    def _send_notification(self, customer_id, message, notification_type):
        """发送通知"""
        print(f"  - 发送通知: 类型={notification_type}, 客户={customer_id}, 消息={message}")
        # 这里可以集成邮件、短信、企业微信等通知方式
        return {"sent": True, "type": notification_type}
    
    def feedback_to_model(self, execution_result, customer_data):
        """
        将执行结果反馈给模型，用于持续优化
        :param execution_result: 执行结果
        :param customer_data: 客户数据
        :return: 反馈状态
        """
        print("正在将执行结果反馈至风控平台，用于模型优化...")
        # 这里可以将结果发送到数据湖或机器学习平台进行模型训练
        feedback_data = {
            "customer_id": customer_data.get("customer_id"),
            "execution_result": execution_result,
            "timestamp": __import__('datetime').datetime.now().isoformat()
        }
        
        # 模拟反馈过程
        print(f"  - 反馈数据: {feedback_data}")
        return {"status": "FEEDBACK_SENT", "data": feedback_data}
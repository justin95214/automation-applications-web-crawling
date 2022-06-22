import smtplib
from email.mime.text import MIMEText
import log_package as lp
import logging

logger = lp.log_setting(logging)

def send_email(title_string, string):
    try:
        # 세션 생성

        s = smtplib.SMTP('smtp.gmail.com', 587)
        # TLS 보안 시작
        s.starttls()

        # 로그인 인증
        mail = "20211302@hansung.ac.kr"
        pwd ="vuwysoppxijmvosd"
        s.login(mail, pwd)

        # 보낼 메시지 설정

        msg = MIMEText(string)
        msg_client = MIMEText(string)

        msg_client = MIMEText("입문증 출력에 오류가 발생했습니다. \n TSP 개발 담당자에게 연락을 보냈습니다.\n 빠른 시일내에 A/S 완료후 보고드리겠습니다 \n 수작업으로 입문증 출력을 확인해주십시오!.")

        msg['Subject'] = title_string
        msg_client['Subject'] = title_string

        # 메일 보내기
        receive_mail1 =mail
        receive_mail2 = "soochan.choi@kurlycorp.com"
        receive_mail3 = "jooyup255@gmail.com"
        receive_mail4 = "bsy8960@naver.com"

        s.sendmail(mail, receive_mail1, msg.as_string())
        s.sendmail(mail, receive_mail2, msg.as_string())
        s.sendmail(mail, receive_mail3,  msg.as_string())
        s.sendmail(mail, receive_mail4, msg.as_string())
        # 세션 종료

        s.quit()
        logger.debug(
            f'fuc >>  send_alert_email :  오류 알람 이메일 송신 완료')
    except:
        logger.error(
            f'fuc >>  send_alert_email :  오류 알람 이메일 송신 실패')

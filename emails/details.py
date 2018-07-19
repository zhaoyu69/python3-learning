#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# MUA：Mail User Agent——邮件用户代理 邮件从这里发出
# MTA：Mail Transfer Agent——邮件传输代理 代理服务商，比如腾讯，网易
# MDA：Mail Delivery Agent——邮件投递代理 邮件到达存放

# 发件人 -> MUA -> MTA -> MTA -> 若干个MTA -> MDA <- MUA <- 收件人
# 发邮件：SMTP
# 收邮件：POP3/IMAP
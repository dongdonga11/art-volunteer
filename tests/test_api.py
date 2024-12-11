import requests
import json
from datetime import datetime

BASE_URL = "http://localhost:3000"  # 修改为本地测试地址

def test_get_schools():
    """测试获取学校列表接口"""
    try:
        response = requests.get(f"{BASE_URL}/api/schools", timeout=10)
        print("\n1. 获取学校列表 - 响应信息")
        print(f"状态码: {response.status_code}")
        
        if response.status_code == 200:
            print(f"响应数据: {json.dumps(response.json(), ensure_ascii=False, indent=2)}")
        else:
            print(f"错误信息: {response.text}")
            
    except requests.exceptions.ConnectionError:
        print("连接错误：无法连接到服务器")
    except requests.exceptions.Timeout:
        print("请求超时")
    except Exception as e:
        print(f"发生错误: {str(e)}")

def test_create_volunteer():
    """测试创建志愿接口"""
    try:
        # 首先获取一个有效的school_id
        response = requests.get(f"{BASE_URL}/api/schools")
        if response.status_code != 200:
            print("无法获取学校列表��跳过创建志愿测试")
            return
            
        schools = response.json()
        if not schools:
            print("学校列表为空，跳过创建志愿测试")
            return
            
        school_id = schools[0]['id']  # 使用第一个学校的ID
        
        # 测试成功场景
        data = {
            "school_id": school_id,
            "user_id": "test_user_001",
            "priority": True
        }
        
        response = requests.post(f"{BASE_URL}/api/volunteers", json=data)
        print("\n2. 创建志愿 - 成功场景")
        print(f"状态码: {response.status_code}")
        print(f"响应数据: {json.dumps(response.json(), ensure_ascii=False, indent=2)}")
        
        # 保存创建的志愿ID用于后续测试
        if response.status_code == 201:
            global created_volunteer_id
            created_volunteer_id = response.json()['id']
        
        # 测试失败场景 - 缺少必要字段
        invalid_data = {
            "school_id": school_id
            # 缺少 user_id
        }
        
        response = requests.post(f"{BASE_URL}/api/volunteers", json=invalid_data)
        print("\n2. 创建志愿 - 失败场景（缺少必要字段）")
        print(f"状态码: {response.status_code}")
        print(f"响应数据: {json.dumps(response.json(), ensure_ascii=False, indent=2)}")
        
    except Exception as e:
        print(f"测试过程中发生错误: {str(e)}")

def test_update_volunteer():
    """测试更新志愿优先级接口"""
    try:
        if not globals().get('created_volunteer_id'):
            print("\n3. 更新志愿优先级 - 跳过（没有可用的志愿ID）")
            return
            
        # 测试成功场景
        response = requests.put(f"{BASE_URL}/api/volunteers/{created_volunteer_id}")
        print("\n3. 更新志愿优先级 - 成功场景")
        print(f"状态码: {response.status_code}")
        if response.status_code == 200:
            print(f"响应数据: {json.dumps(response.json(), ensure_ascii=False, indent=2)}")
        else:
            print(f"错误信息: {response.text}")
        
        # 测试失败场景 - 无效ID
        invalid_id = 99999
        response = requests.put(f"{BASE_URL}/api/volunteers/{invalid_id}")
        print("\n3. 更新志愿优先级 - 失败场景（无效ID）")
        print(f"状态码: {response.status_code}")
        print(f"响应数据: {json.dumps(response.json(), ensure_ascii=False, indent=2)}")
        
    except Exception as e:
        print(f"测试过程中发生错误: {str(e)}")

def test_delete_volunteer():
    """测试删除志愿接口"""
    try:
        if not globals().get('created_volunteer_id'):
            print("\n4. 删除志愿 - 跳过（没有可用的志愿ID）")
            return
            
        # 测试成功场景
        response = requests.delete(f"{BASE_URL}/api/volunteers/{created_volunteer_id}")
        print("\n4. 删除志愿 - 成功场景")
        print(f"状态码: {response.status_code}")
        if response.status_code == 200:
            print(f"响应数据: {json.dumps(response.json(), ensure_ascii=False, indent=2)}")
        else:
            print(f"错误信息: {response.text}")
        
        # 测试失败场景 - 不存在的ID
        non_existent_id = 99999
        response = requests.delete(f"{BASE_URL}/api/volunteers/{non_existent_id}")
        print("\n4. 删除志愿 - 失败场景（不存在的ID）")
        print(f"状态码: {response.status_code}")
        print(f"响应数据: {json.dumps(response.json(), ensure_ascii=False, indent=2)}")
        
    except Exception as e:
        print(f"测试过程中发生错误: {str(e)}")

if __name__ == "__main__":
    print("开始测试艺术生志愿填报系统API...")
    test_get_schools()
    test_create_volunteer()
    test_update_volunteer()
    test_delete_volunteer()
    print("\n测试完成！") 
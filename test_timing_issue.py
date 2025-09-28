#!/usr/bin/env python3
"""
Test Timing Issue
Test the scheduler timing problem
"""

import os
import sys
import time
import logging
from datetime import datetime, timedelta
import pytz
from scheduler import scheduler

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('timing_test.log'),
        logging.StreamHandler()
    ]
)

def test_scheduler_timing():
    """Test the scheduler timing issue"""
    print("🧪 TESTING SCHEDULER TIMING ISSUE")
    print("=" * 50)
    
    # Get current time
    ist = pytz.timezone('Asia/Kolkata')
    current_time = datetime.now(ist)
    print(f"🕐 Current IST time: {current_time.strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Show configured upload times
    print(f"📅 Configured upload times: {scheduler.upload_times}")
    
    # Check if current time matches any upload time
    current_time_str = current_time.strftime('%H:%M')
    print(f"🔍 Current time string: {current_time_str}")
    
    for upload_time in scheduler.upload_times:
        if current_time_str == upload_time:
            print(f"✅ MATCH: Current time {current_time_str} matches upload time {upload_time}")
        else:
            print(f"❌ NO MATCH: Current time {current_time_str} != upload time {upload_time}")
    
    # Test manual trigger
    print(f"\n🧪 Testing manual trigger for {current_time_str}")
    try:
        success = scheduler.force_trigger_upload(current_time_str)
        if success:
            print("✅ Manual trigger: SUCCESS")
        else:
            print("❌ Manual trigger: FAILED")
    except Exception as e:
        print(f"❌ Manual trigger error: {e}")

def monitor_scheduler_for_time(target_time, duration_minutes=5):
    """Monitor scheduler for a specific time"""
    print(f"\n👀 MONITORING FOR TIME: {target_time}")
    print("=" * 50)
    
    start_time = datetime.now()
    end_time = start_time + timedelta(minutes=duration_minutes)
    
    check_count = 0
    while datetime.now() < end_time:
        check_count += 1
        current_time = datetime.now()
        current_time_str = current_time.strftime('%H:%M')
        
        print(f"\n🔍 Check #{check_count} - {current_time_str}")
        
        if current_time_str == target_time:
            print(f"🚨 TARGET TIME REACHED: {target_time}")
            print("🚨 This is when the upload should trigger!")
            
            # Wait a bit more to see if it triggers
            for i in range(6):  # Wait 30 seconds
                time.sleep(5)
                print(f"⏳ Waiting... {i+1}/6")
        
        time.sleep(10)  # Check every 10 seconds
    
    print(f"\n✅ Monitoring completed after {duration_minutes} minutes")

def main():
    """Main test function"""
    if len(sys.argv) > 1:
        command = sys.argv[1].lower()
        
        if command == "timing":
            test_scheduler_timing()
        elif command == "monitor":
            if len(sys.argv) > 2:
                target_time = sys.argv[2]
                duration = int(sys.argv[3]) if len(sys.argv) > 3 else 5
                monitor_scheduler_for_time(target_time, duration)
            else:
                print("Usage: python test_timing_issue.py monitor <time> [duration]")
        else:
            print("Unknown command. Use 'timing' or 'monitor <time>'")
    else:
        print("""
Timing Issue Test

Commands:
  python test_timing_issue.py timing           - Test current timing
  python test_timing_issue.py monitor <time>  - Monitor for specific time
        """)

if __name__ == "__main__":
    main()

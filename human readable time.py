def format_duration(seconds):
  """Formats time in seconds to human readable time. Did not include months."""
    def minute(seconds):
        if seconds < 60:
            if seconds == 0: return "now"
            if seconds == 1:
                return "1 second"
            else: return f"{seconds} seconds"
        elif seconds < 3600:
            if seconds % 60 == 0:
                if seconds // 60 == 1: return f"{seconds//60} minute"
                else: return f"{seconds//60} minutes"
            else:
                if seconds // 60 == 1 and seconds % 60 == 1: return "1 minute and 1 second"
                elif seconds // 60 == 1: return f"1 minute and {seconds%60} seconds"
                elif seconds % 60 == 1: return f"{seconds // 60} minutes and {seconds % 60} second"
                else: return f"{seconds // 60} minutes and {seconds % 60} seconds"
            
    def hours(seconds):
        hour = seconds // 3600
        if seconds == 3600: return "1 hour"
        else:
            if hour == 0: return minute(seconds)
            elif hour == 1 and seconds % 60 > 0: return f"{hour} hour, {minute(seconds % 3600)}"
            elif hour ==1 and seconds % 60 == 0: return f"{hour} hour and {minute(seconds % 3600)}"
            elif hour > 1 and seconds % 60 == 0: return f"{hour} hours and {minute(seconds % 3600)}"
            elif hour > 1 and seconds % 3600 < 60: return f"{hour} hours and {minute(seconds % 3600)}"
            else: return f"{hour} hours, {minute(seconds % 3600)}"
        
    def day(seconds):
            if (seconds//3600) > 24:
                days = (seconds//3600) // 24
                if seconds == 86400: return "1 day"
                else:
                    if days == 1: return f"1 day, {hours(seconds % 86400)}"
                    elif days == 1 and (seconds%86400)//3600 == 0 and ((seconds%86400)%3600)//60 == 0 and seconds % 60 !=0:
                        return f"1 day and {hours(seconds % 86400)}"
                    elif days == 1 and (seconds%86400)//3600 == 0 and ((seconds%86400)%3600)//60 != 0 and seconds % 60 ==0:
                        return f"1 day and {hours(seconds % 86400)}"   
                    elif days == 1 and (seconds%86400)//3600 != 0 and ((seconds%86400)%3600)//60 == 0 and seconds % 60 ==0:
                        return f"1 day and {hours(seconds % 86400)}"  
                    elif days > 1 and (seconds%86400)//3600 == 0 and ((seconds%86400)%3600)//60 == 0 and seconds % 60 !=0:
                        return f"{days} days and {hours(seconds % 86400)}"
                    elif days > 1 and (seconds%86400)//3600 == 0 and ((seconds%86400)%3600)//60 != 0 and seconds % 60 ==0:
                        return f"{days} days and {hours(seconds % 86400)}" 
                    elif days == 1 and (seconds%86400)//3600 != 0 and ((seconds%86400)%3600)//60 == 0 and seconds % 60 ==0:
                        return f"{days} days and {hours(seconds % 86400)}" 
                    else: return f"{days} days, {hours(seconds % 86400)}"  
        
        
    if seconds < 3600: return minute(seconds)
    elif seconds < 86400: return hours(seconds)
    elif (seconds//3600)//24 < 365: return day(seconds)
    else:
        years = (seconds // 86400) // 365
        if years == 1 and seconds % 86400 == 0 and seconds // 86400 == 0:
            return f"{years} year"
        elif years == 1 and seconds % 86400 == 0:
            return f"{years} year and {day(seconds % 31536000)}"
        elif years == 1:
            return f"{years} year, {day(seconds % 31536000)}"
        elif years > 1 and seconds % 86400 == 0 and seconds // 86400 == 0:
            return f"{years} years"
        elif years > 1 and seconds % 86400 == 0:
            return f"{years} year and {day(seconds % 31536000)}"
        else:
            return f"{years} years, {day(seconds % 31536000)}"
           

# find . -name *.sql | xargs printf "\"%s\", \n"
# Reorder file order to contain ./mysql_config/Tables/* first

SQL_INIT_FILES = [
    "./mysql_config/Tables/create-tables.sql",
    "./mysql_config/Tables/audit_users_table.sql",
    "./mysql_config/Mocks/insert-values.sql",
    "./mysql_config/WebMonitoring/procedures/resource_get_time.sql",
    "./mysql_config/WebMonitoring/procedures/resource_get_size.sql",
    "./mysql_config/WebMonitoring/procedures/resource_get_old_size.sql",
    "./mysql_config/WebMonitoring/procedures/resource_get_old_time.sql",
    "./mysql_config/WebMonitoring/procedures/samples_time_websites/get_monthly_samples_websites.sql",
    "./mysql_config/WebMonitoring/procedures/samples_time_websites/get_daily_samples_websites.sql",
    "./mysql_config/WebMonitoring/procedures/samples_time_websites/get_weekly_samples_websites.sql",
    "./mysql_config/WebMonitoring/procedures/samples_time_resource/get_daily_samples.sql",
    "./mysql_config/WebMonitoring/procedures/samples_time_resource/get_weekly_samples.sql",
    "./mysql_config/WebMonitoring/procedures/samples_time_resource/get_monthly_samples.sql",
    "./mysql_config/WebMonitoring/procedures/samples_size_resource/get_monthly_samples_size.sql",
    "./mysql_config/WebMonitoring/procedures/samples_size_resource/get_weekly_samples_size.sql",
    "./mysql_config/WebMonitoring/procedures/samples_size_resource/get_daily_samples_size.sql",
    "./mysql_config/WebMonitoring/procedures/samples_size_websites/get_monthly_samples_size_websites.sql",
    "./mysql_config/WebMonitoring/procedures/samples_size_websites/get_daily_samples_size_websites.sql",
    "./mysql_config/WebMonitoring/procedures/samples_size_websites/get_weekly_samples_size_websites.sql",
    "./mysql_config/WebMonitoring/functions/resource_get_availability.sql",
    "./mysql_config/WebMonitoring/functions/resource_statistics_size/resource_statistics_last_24_size/resource_statistic_average_size_24.sql",
    "./mysql_config/WebMonitoring/functions/resource_statistics_size/resource_statistics_last_24_size/resource_statistic_standard_deviation_size_24.sql",
    "./mysql_config/WebMonitoring/functions/resource_statistics_size/resource_statistics_last_24_size/resource_statistic_size_24.sql",
    "./mysql_config/WebMonitoring/functions/resource_statistics_size/resource_statistics_all_size/resource_statistic_size.sql",
    "./mysql_config/WebMonitoring/functions/resource_statistics_size/resource_statistics_all_size/resource_statistic_standard_deviation_size.sql",
    "./mysql_config/WebMonitoring/functions/resource_statistics_size/resource_statistics_all_size/resource_statistic_average_size.sql",
    "./mysql_config/WebMonitoring/functions/resource_statistics_time/resource_statistics_last_24_time/resource_statistic_requests_time_24.sql",
    "./mysql_config/WebMonitoring/functions/resource_statistics_time/resource_statistics_last_24_time/resource_statistic_average_time_24.sql",
    "./mysql_config/WebMonitoring/functions/resource_statistics_time/resource_statistics_last_24_time/resource_statistic_standard_deviation_time_24.sql",
    "./mysql_config/WebMonitoring/functions/resource_statistics_time/resource_statistics_last_24_time/resource_statistic_time_24.sql",
    "./mysql_config/WebMonitoring/functions/resource_statistics_time/resource_statistics_all_time/resource_statistic_time.sql",
    "./mysql_config/WebMonitoring/functions/resource_statistics_time/resource_statistics_all_time/resource_statistic_standard_deviation_time.sql",
    "./mysql_config/WebMonitoring/functions/resource_statistics_time/resource_statistics_all_time/resource_statistic_requests_time.sql",
    "./mysql_config/WebMonitoring/functions/resource_statistics_time/resource_statistics_all_time/resource_statistic_average_time.sql",
    "./mysql_config/Login/triggers/trigger.sql",
]

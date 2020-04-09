# How to beautify JSX

## Also works on YAMLs, MDs, JSONs

### Installation
```
raress-mbp:rafMetrics raresfolea$ npm install --global prettier
/usr/local/bin/prettier -> /usr/local/lib/node_modules/prettier/bin-prettier.js
+ prettier@2.0.4
added 1 package from 1 contributor in 0.947s
```

### Usage
```
raress-mbp:rafMetrics raresfolea$ prettier --write .
```

### Sample Output
```
.devbots/needs-triage.yml 44ms
.github/stale.yml 8ms
.github/workflows/codecov.yml 13ms
.github/workflows/pythonapp.yml 10ms
.pytest_cache/README.md 32ms
codecov.yml 5ms
docker_config/docker-compose.yaml 34ms
docker_config/README.md 11ms
grafana/rafMetrics-1585565200101.json 77ms
kubernetes_config/database/mysql-deployment.yaml 18ms
kubernetes_config/database/mysql-pv.yaml 6ms
kubernetes_config/latest/deployment_resource.yaml 7ms
kubernetes_config/latest/deployment_website.yaml 8ms
kubernetes_config/latest/login.yaml 10ms
kubernetes_config/latest/metricsui.yaml 6ms
kubernetes_config/latest/webmonitoringapi.yaml 12ms
kubernetes_config/README.md 16ms
kubernetes_config/templates/template_deployment_resource.yaml 6ms
kubernetes_config/templates/template_deployment_website.yaml 11ms
kubernetes_config/templates/template_login.yaml 14ms
kubernetes_config/templates/template_metricsui.yaml 8ms
kubernetes_config/templates/template_webmonitoringapi.yaml 16ms
Login/README.md 28ms
metricsUI/jsconfig.json 5ms
metricsUI/package-lock.json 337ms
metricsUI/package.json 41ms
metricsUI/public/index.html 84ms
metricsUI/public/manifest.json 4ms
metricsUI/README.md 36ms
metricsUI/src/components/App.js 40ms
metricsUI/src/components/Header/Header.js 39ms
metricsUI/src/components/Header/package.json 10ms
metricsUI/src/components/Header/styles.js 29ms
metricsUI/src/components/Layout/Layout.js 10ms
metricsUI/src/components/Layout/package.json 3ms
metricsUI/src/components/Layout/styles.js 7ms
metricsUI/src/components/PageTitle/package.json 5ms
metricsUI/src/components/PageTitle/PageTitle.js 6ms
metricsUI/src/components/PageTitle/styles.js 6ms
metricsUI/src/components/Sidebar/components/Dot.js 8ms
metricsUI/src/components/Sidebar/components/SidebarLink/SidebarLink.js 20ms
metricsUI/src/components/Sidebar/components/SidebarLink/styles.js 18ms
metricsUI/src/components/Sidebar/package.json 2ms
metricsUI/src/components/Sidebar/Sidebar.js 29ms
metricsUI/src/components/Sidebar/SidebarView.js 26ms
metricsUI/src/components/Sidebar/styles.js 12ms
metricsUI/src/components/UserAvatar/package.json 2ms
metricsUI/src/components/UserAvatar/styles.js 2ms
metricsUI/src/components/UserAvatar/UserAvatar.js 8ms
metricsUI/src/components/Widget/package.json 4ms
metricsUI/src/components/Widget/styles.js 7ms
metricsUI/src/components/Widget/Widget.js 21ms
metricsUI/src/components/Widget/WidgetView.js 15ms
metricsUI/src/components/Wrappers/package.json 2ms
metricsUI/src/components/Wrappers/Wrappers.js 16ms
metricsUI/src/config.js 6ms
metricsUI/src/context/LayoutContext.js 11ms
metricsUI/src/context/ResourceContext.js 7ms
metricsUI/src/context/UserContext.js 21ms
metricsUI/src/index.js 10ms
metricsUI/src/pages/dashboard/components/BigStat/BigStat.js 23ms
metricsUI/src/pages/dashboard/components/BigStat/BigStatResource.js 15ms
metricsUI/src/pages/dashboard/components/BigStat/styles.js 4ms
metricsUI/src/pages/dashboard/components/Table/Table.js 10ms
metricsUI/src/pages/dashboard/components/Table/TableResource.js 11ms
metricsUI/src/pages/dashboard/components/Table/TableWebsites.js 19ms
metricsUI/src/pages/dashboard/Dashboard.js 5ms
metricsUI/src/pages/dashboard/DashboardResource.js 44ms
metricsUI/src/pages/dashboard/DashboardResourceStatistics.js 26ms
metricsUI/src/pages/dashboard/DashboardWebsite.js 39ms
metricsUI/src/pages/dashboard/DashboardWebsiteStatistics.js 25ms
metricsUI/src/pages/dashboard/mock.js 29ms
metricsUI/src/pages/dashboard/package.json 1ms
metricsUI/src/pages/dashboard/styles.js 13ms
metricsUI/src/pages/error/Error.js 6ms
metricsUI/src/pages/error/package.json 1ms
metricsUI/src/pages/error/styles.js 5ms
metricsUI/src/pages/icons/Icons.js 830ms
metricsUI/src/pages/icons/package.json 2ms
metricsUI/src/pages/icons/styles.js 3ms
metricsUI/src/pages/login/Login.js 17ms
metricsUI/src/pages/login/package.json 1ms
metricsUI/src/pages/login/styles.js 16ms
metricsUI/src/serviceWorker.js 33ms
metricsUI/src/themes/default.js 8ms
metricsUI/src/themes/index.js 3ms
mysql_config/README.md 172ms
mysql_config/WebMonitoring/procedures/samples_size_resource/README.md 8ms
mysql_config/WebMonitoring/procedures/samples_size_websites/README.md 4ms
mysql_config/WebMonitoring/sampleHARrecords/71ZVr6zU.json 146ms
mysql_config/WebMonitoring/sampleHARrecords/bvLQwmca.json 44ms
mysql_config/WebMonitoring/sampleHARrecords/uEPPEjA8.json 56ms
rafComputing/README.md 6ms
rafComputing/UCU/README.md 2ms
README.md 11ms
tests/README.md 3ms
WebMonitoring/API/README.md 38ms
WebMonitoring/README.md 5ms
WebMonitoring/WebsiteMonitorHelpers/README.md 3ms
```
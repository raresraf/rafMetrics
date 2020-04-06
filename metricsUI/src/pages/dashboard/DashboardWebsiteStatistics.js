import React, {useState} from "react";
import {Grid,} from "@material-ui/core";
import {useTheme} from "@material-ui/styles";
import {Line, LineChart,} from "recharts";
// styles
import useStyles from "./styles";
// components
import mock from "./mock";
import Widget from "../../components/Widget";
import PageTitle from "../../components/PageTitle";
import {Typography} from "../../components/Wrappers";


import {backend_webmonitoringapi_ip} from '../../config';


function getDashboardWebsiteStatistics() {
  return new Promise((resolve, reject) => {
    let availableResourcesUrl = backend_webmonitoringapi_ip + "/websites/statistics";
    fetch(availableResourcesUrl)
      .then((response) => {
        return response.json();
      })
      .then((jsonResponse) => {
        resolve(jsonResponse);
      })
      .catch((err) => {
        reject(err);
      });
  })
}

export default function DashboardWebsiteStatistics(props) {
  var classes = useStyles();
  var theme = useTheme();

  const [DashboardWebsiteStatistics, setDashboardWebsiteStatistics] = useState(mock.resourcestatistics);
  const [getDashboardWebsiteStatisticsLoaded, setDashboardWebsiteStatisticsLoaded] = useState(false );

  if(!getDashboardWebsiteStatisticsLoaded){
    setDashboardWebsiteStatisticsLoaded(true);
    getDashboardWebsiteStatistics().then(res => {
      setDashboardWebsiteStatistics(res);
    });
  }

  return (
        <>
          <PageTitle title="Statistics Website Manager"
          />
          <Grid container spacing={2}>
            <Grid item lg={6} md={6} sm={6} xs={12}>
              <Widget
                title="Last 24 hours"
                upperTitle
                bodyClass={classes.fullHeightBody}
                className={classes.card}
              >
                <div className={classes.visitsNumberContainer}>
                  <Typography size="xl" weight="medium">
                    ⌛: {DashboardWebsiteStatistics['time_24']}
                  </Typography>
                  <LineChart
                    width={55}
                    height={30}
                    data={[
                      { value: 10 },
                      { value: 15 },
                      { value: 10 },
                      { value: 17 },
                      { value: 18 },
                    ]}
                    margin={{ left: theme.spacing(2) }}
                  >
                    <Line
                      type="natural"
                      dataKey="value"
                      stroke={theme.palette.success.main}
                      strokeWidth={2}
                      dot={false}
                    />
                  </LineChart>
                </div>
                <Grid
                  container
                  direction="row"
                  justify="space-between"
                  alignItems="center"
                >
                  <Grid item>
                    <Typography color="text" colorBrightness="secondary">
                      Requests
                    </Typography>
                    <Typography size="md">{DashboardWebsiteStatistics['requests_24']}</Typography>
                  </Grid>
                  <Grid item>
                    <Typography color="text" colorBrightness="secondary">
                      Average Time
                    </Typography>
                    <Typography size="md">{DashboardWebsiteStatistics['average_time_24']}</Typography>
                  </Grid>
                  <Grid item>
                    <Typography color="text" colorBrightness="secondary">
                      Standard deviation
                    </Typography>
                    <Typography size="md">{DashboardWebsiteStatistics['sd_time_24']}</Typography>
                  </Grid>
                </Grid>
              </Widget>
            </Grid>
            <Grid item lg={6} md={6} sm={6} xs={12}>
              <Widget
                title="All time 📅"
                upperTitle
                bodyClass={classes.fullHeightBody}
                className={classes.card}
              >
                <div className={classes.visitsNumberContainer}>
                  <Typography size="xl" weight="medium">
                    ⌛: {DashboardWebsiteStatistics['time_all']}
                  </Typography>
                  <LineChart
                    width={55}
                    height={30}
                    data={[
                      { value: 10 },
                      { value: 15 },
                      { value: 10 },
                      { value: 17 },
                      { value: 18 },
                    ]}
                    margin={{ left: theme.spacing(2) }}
                  >
                    <Line
                      type="natural"
                      dataKey="value"
                      stroke={theme.palette.success.main}
                      strokeWidth={2}
                      dot={false}
                    />
                  </LineChart>
                </div>
                <Grid
                  container
                  direction="row"
                  justify="space-between"
                  alignItems="center"
                >
                  <Grid item>
                    <Typography color="text" colorBrightness="secondary">
                      Requests
                    </Typography>
                    <Typography size="md">{DashboardWebsiteStatistics['requests_all']}</Typography>
                  </Grid>
                  <Grid item>
                    <Typography color="text" colorBrightness="secondary">
                      Average Time
                    </Typography>
                    <Typography size="md">{DashboardWebsiteStatistics['average_time_all']}</Typography>
                  </Grid>
                  <Grid item>
                    <Typography color="text" colorBrightness="secondary">
                      Standard deviation
                    </Typography>
                    <Typography size="md">{DashboardWebsiteStatistics['sd_time_all']}</Typography>
                  </Grid>
                </Grid>
              </Widget>
            </Grid>
          </Grid>
          <Grid container spacing={2}>
            <Grid item lg={6} md={6} sm={6} xs={12}>
              <Widget
                title="Last 24 hours"
                upperTitle
                bodyClass={classes.fullHeightBody}
                className={classes.card}
              >
                <div className={classes.visitsNumberContainer}>
                  <Typography size="xl" component={'span'} weight="medium">
                    <Typography size="md">Bytes: {DashboardWebsiteStatistics['size_24']}</Typography>
                  </Typography>
                  <LineChart
                    width={55}
                    height={30}
                    data={[
                      { value: 10 },
                      { value: 15 },
                      { value: 10 },
                      { value: 17 },
                      { value: 18 },
                    ]}
                    margin={{ left: theme.spacing(2) }}
                  >
                    <Line
                      type="natural"
                      dataKey="value"
                      stroke={theme.palette.success.main}
                      strokeWidth={2}
                      dot={false}
                    />
                  </LineChart>
                </div>
                <Grid
                  container
                  direction="row"
                  justify="space-between"
                  alignItems="center"
                >
                  <Grid item>
                    <Typography color="text" colorBrightness="secondary">
                      Average Size
                    </Typography>
                    <Typography size="md">{DashboardWebsiteStatistics['average_size_24']}</Typography>
                  </Grid>
                  <Grid item>
                    <Typography color="text" colorBrightness="secondary">
                      Standard deviation
                    </Typography>
                    <Typography size="md">{DashboardWebsiteStatistics['sd_size_24']}</Typography>
                  </Grid>
                </Grid>
              </Widget>
            </Grid>
            <Grid item lg={6} md={6} sm={6} xs={12}>
              <Widget
                title="All time 📅"
                upperTitle
                bodyClass={classes.fullHeightBody}
                className={classes.card}
              >
                <div className={classes.visitsNumberContainer}>
                  <Typography size="xl" component={'span'} weight="medium">
                    <Typography size="md">Bytes: {DashboardWebsiteStatistics['size_all']}</Typography>
                  </Typography>
                  <LineChart
                    width={55}
                    height={30}
                    data={[
                      { value: 10 },
                      { value: 15 },
                      { value: 10 },
                      { value: 17 },
                      { value: 18 },
                    ]}
                    margin={{ left: theme.spacing(2) }}
                  >
                    <Line
                      type="natural"
                      dataKey="value"
                      stroke={theme.palette.success.main}
                      strokeWidth={2}
                      dot={false}
                    />
                  </LineChart>
                </div>
                <Grid
                  container
                  direction="row"
                  justify="space-between"
                  alignItems="center"
                >
                  <Grid item>
                    <Typography color="text" colorBrightness="secondary">
                      Average Size
                    </Typography>
                    <Typography size="md">{DashboardWebsiteStatistics['average_size_all']}</Typography>
                  </Grid>
                  <Grid item>
                    <Typography color="text" colorBrightness="secondary">
                      Standard deviation
                    </Typography>
                    <Typography size="md">{DashboardWebsiteStatistics['sd_size_all']}</Typography>
                  </Grid>
                </Grid>
              </Widget>
            </Grid>
          </Grid>



        </>
    );


}

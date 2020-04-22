import React, {useState} from "react";
import {Grid, MenuItem, OutlinedInput, Select} from "@material-ui/core";
import {useTheme} from "@material-ui/styles";
import {Area, ComposedChart, Line, ResponsiveContainer, XAxis, YAxis,} from "recharts";
// styles
import useStyles from "./styles";
// components
import mock from "./mock";
import Widget from "../../components/Widget";
import PageTitle from "../../components/PageTitle";
import {Typography} from "../../components/Wrappers";
import Dot from "../../components/Sidebar/components/Dot";
import TableResource from "./components/Table/TableResource";
import BigStatResource from "./components/BigStat/BigStatResource";
import {useUserState} from "../../context/UserContext";
import {useResourceState} from "../../context/ResourceContext";
import {backend_webmonitoringapi_ip} from "../../config";

function getAvailableResources(username) {
  return new Promise((resolve, reject) => {
    let availableResourcesUrl =
      backend_webmonitoringapi_ip + "/availableResources/" + username;
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
  });
}

function getRequestTime(resourceid) {
  return new Promise((resolve, reject) => {
    let availableResourcesUrl =
      backend_webmonitoringapi_ip + "/resources/metrics/" + resourceid;
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
  });
}

function getSamplesTime(period, resourceid) {
  return new Promise((resolve, reject) => {
    let availableResourcesUrl =
      backend_webmonitoringapi_ip +
      "/resources/samples/time/" +
      resourceid +
      "/" +
      period;
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
  });
}

function getSamplesSize(period, resourceid) {
  return new Promise((resolve, reject) => {
    let availableResourcesUrl =
      backend_webmonitoringapi_ip +
      "/resources/samples/size/" +
      resourceid +
      "/" +
      period;
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
  });
}

function refresh_DashboardResource(
  setAvailableResourcesLoaded,
  setRequestTimeLoaded,
  setSamplesTimeLoaded,
  setSamplesSizeLoaded
) {
  setAvailableResourcesLoaded(false);
  setRequestTimeLoaded(false);
  setSamplesTimeLoaded(false);
  setSamplesSizeLoaded(false);
}

export default function DashboardResource(props) {
  console.log(props);
  var classes = useStyles();
  var theme = useTheme();

  // local
  const [tableResource, setTableResource] = useState(mock.tableResource);
  const [bigStatResource, setBigStatResource] = useState(mock.bigStatResource);

  const [samplesTime, setSamplesTime] = useState(mock.samples_time);
  const [samplesSize, setSamplesSize] = useState(mock.samples_time);

  var [timeChartState, setTimeChartState] = useState("daily");
  var [sizeChartState, setSizeChartState] = useState("daily");

  const [getAvailableResourcesLoaded, setAvailableResourcesLoaded] = useState(
    false
  );
  const [getRequestTimeLoaded, setRequestTimeLoaded] = useState(false);
  const [getSamplesTimeLoaded, setSamplesTimeLoaded] = useState(false);
  const [getSamplesSizeLoaded, setSamplesSizeLoaded] = useState(false);

  var { username } = useUserState();
  var { resourceid } = useResourceState();

  if (!getAvailableResourcesLoaded) {
    setAvailableResourcesLoaded(true);
    getAvailableResources(username).then((res) => {
      setTableResource(res);
    });
  }

  if (!getRequestTimeLoaded) {
    setRequestTimeLoaded(true);
    getRequestTime(resourceid).then((res) => {
      setBigStatResource(res);
    });
  }

  if (!getSamplesTimeLoaded) {
    setSamplesTimeLoaded(true);
    getSamplesTime(timeChartState, resourceid).then((res) => {
      setSamplesTime(res);
    });
  }

  if (!getSamplesSizeLoaded) {
    setSamplesSizeLoaded(true);
    getSamplesSize(sizeChartState, resourceid).then((res) => {
      setSamplesSize(res);
    });
  }
  return (
    <>
      <PageTitle title="Dashboard Resources" button="See all resources" />
      <Grid container spacing={4}>
        <Grid item xs={12}>
          <Widget
            title="Choose Resourse"
            upperTitle
            noBodyPadding
            bodyClass={classes.tableWidget}
          >
            <TableResource
              data={tableResource}
              p1={setRequestTimeLoaded}
              p2={setSamplesTimeLoaded}
              p3={setSamplesSizeLoaded}
            />
          </Widget>
        </Grid>

        <Grid item xs={12}>
          <Widget
            bodyClass={classes.mainChartBody}
            header={
              <div className={classes.mainChartHeader}>
                <Typography
                  variant="h5"
                  color="text"
                  colorBrightness="secondary"
                >
                  Response Time
                </Typography>
                <div className={classes.mainChartHeaderLabels}>
                  <div className={classes.mainChartHeaderLabel}>
                    <Dot color="primary" />
                    <Typography className={classes.mainChartLegentElement}>
                      Response Time (seconds)
                    </Typography>
                  </div>
                </div>
                <Select
                  value={timeChartState}
                  onChange={(e) => {
                    setTimeChartState(e.target.value);
                    refresh_DashboardResource(
                      setAvailableResourcesLoaded,
                      setRequestTimeLoaded,
                      setSamplesTimeLoaded,
                      setSamplesSizeLoaded
                    );
                  }}
                  input={
                    <OutlinedInput
                      labelWidth={0}
                      classes={{
                        notchedOutline: classes.mainChartSelectRoot,
                        input: classes.mainChartSelect,
                      }}
                    />
                  }
                  autoWidth
                >
                  <MenuItem value="daily">Daily</MenuItem>
                  <MenuItem value="weekly">Weekly</MenuItem>
                  <MenuItem value="monthly">Monthly</MenuItem>
                </Select>
              </div>
            }
          >
            <ResponsiveContainer width="100%" minWidth={500} height={350}>
              <ComposedChart
                margin={{ top: 0, right: -15, left: -15, bottom: 0 }}
                data={samplesTime}
              >
                <YAxis
                  tick={{ fill: theme.palette.text.hint + "80", fontSize: 14 }}
                  stroke={theme.palette.text.hint + "80"}
                  tickLine={false}
                />
                <XAxis
                  tickFormatter={(i) => samplesTime[i]["label"]}
                  tick={{ fill: theme.palette.text.hint + "80", fontSize: 14 }}
                  stroke={theme.palette.text.hint + "80"}
                  tickLine={false}
                />
                <Area
                  type="natural"
                  dataKey="custom_data"
                  fill={theme.palette.background.light}
                  strokeWidth={0}
                  activeDot={false}
                />
                <Line
                  type="natural"
                  dataKey="custom_data"
                  stroke={theme.palette.primary.main}
                  strokeWidth={2}
                  dot={{
                    stroke: theme.palette.primary.dark,
                    strokeWidth: 2,
                    fill: theme.palette.primary.main,
                  }}
                />
              </ComposedChart>
            </ResponsiveContainer>
          </Widget>
        </Grid>

        <Grid item xs={12}>
          <Widget
            bodyClass={classes.mainChartBody}
            header={
              <div className={classes.mainChartHeader}>
                <Typography
                  variant="h5"
                  color="text"
                  colorBrightness="secondary"
                >
                  Response Size (kB)
                </Typography>
                <div className={classes.mainChartHeaderLabels}>
                  <div className={classes.mainChartHeaderLabel}>
                    <Dot color="warning" />
                    <Typography className={classes.mainChartLegentElement}>
                      Response Size
                    </Typography>
                  </div>
                </div>
                <Select
                  value={sizeChartState}
                  onChange={(e) => {
                    setSizeChartState(e.target.value);
                    refresh_DashboardResource(
                      setAvailableResourcesLoaded,
                      setRequestTimeLoaded,
                      setSamplesTimeLoaded,
                      setSamplesSizeLoaded
                    );
                  }}
                  input={
                    <OutlinedInput
                      labelWidth={0}
                      classes={{
                        notchedOutline: classes.mainChartSelectRoot,
                        input: classes.mainChartSelect,
                      }}
                    />
                  }
                  autoWidth
                >
                  <MenuItem value="daily">Daily</MenuItem>
                  <MenuItem value="weekly">Weekly</MenuItem>
                  <MenuItem value="monthly">Monthly</MenuItem>
                </Select>
              </div>
            }
          >
            <ResponsiveContainer width="100%" minWidth={500} height={350}>
              <ComposedChart
                margin={{ top: 0, right: -15, left: -15, bottom: 0 }}
                data={samplesSize}
              >
                <YAxis
                  tick={{ fill: theme.palette.text.hint + "80", fontSize: 14 }}
                  stroke={theme.palette.text.hint + "80"}
                  tickLine={false}
                />
                <XAxis
                  tickFormatter={(i) => samplesSize[i]["label"]}
                  tick={{ fill: theme.palette.text.hint + "80", fontSize: 14 }}
                  stroke={theme.palette.text.hint + "80"}
                  tickLine={false}
                />
                <Area
                  type="natural"
                  dataKey="custom_data"
                  fill={theme.palette.background.light}
                  strokeWidth={0}
                  activeDot={false}
                />
                <Line
                  type="natural"
                  dataKey="custom_data"
                  stroke={theme.palette.warning.main}
                  strokeWidth={2}
                  dot={{
                    stroke: theme.palette.warning.dark,
                    strokeWidth: 2,
                    fill: theme.palette.warning.main,
                  }}
                />
              </ComposedChart>
            </ResponsiveContainer>
          </Widget>
        </Grid>

        {bigStatResource.map((stat) => (
          <Grid item md={4} sm={6} xs={12} key={stat.product}>
            <BigStatResource {...stat} />
          </Grid>
        ))}
      </Grid>
    </>
  );
}

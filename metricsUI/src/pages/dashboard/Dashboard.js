import React from "react";
import { Button, Grid } from "@material-ui/core";
// styles
// components

export default function Dashboard(props) {
  return (
    <>
      <Grid container spacing={4}>
        <Grid item xs={12}>
          <Button
            variant="contained"
            color="primary"
            onClick={() => props.history.push("/app/ui/resourcemanager")}
            size="large"
          >
            Resource Manager Dashboard
          </Button>
        </Grid>
        <Grid item xs={12}>
          <Button
            variant="contained"
            color="primary"
            onClick={() => props.history.push("/app/ui/websitemanager")}
            size="large"
          >
            Website Manager Dashboard
          </Button>
        </Grid>
      </Grid>
    </>
  );
}

import React from "react";
import {Table, TableBody, TableCell, TableHead, TableRow,} from "@material-ui/core";
// components
import {Button} from "../../../../components/Wrappers";
import {updateResource, useResourceDispatch} from "../../../../context/ResourceContext";

const states = {
  working: "success",
  pending: "warning",
  unavailable: "secondary",
};


export default function TableComponentResource({ data }, method) {

  var resourceDispatch = useResourceDispatch();

  var keys = Object.keys(data[0]).map(i => i.toUpperCase());
  keys.shift(); // delete "id" key

  return (
    <Table className="mb-0">
      <TableHead>
        <TableRow>
          <TableCell key={0}>{'ID'}</TableCell>
          <TableCell key={1}>{'ResourceURL'}</TableCell>
          <TableCell key={2}>{'Command'}</TableCell>
          <TableCell key={3}>{'First Added'}</TableCell>
          <TableCell key={4}>{'Status'}</TableCell>
        </TableRow>
      </TableHead>
      <TableBody>
        {data.map(({ id, id_resource, name, command, firstadded, status }) => (
          <TableRow key={id}>
            <TableCell>{id_resource}</TableCell>
            <TableCell className="pl-3 fw-normal">{name}</TableCell>
            <TableCell>{command}</TableCell>
            <TableCell>{firstadded}</TableCell>
            <TableCell>
              <Button
                color={states[status.toLowerCase()]}
                size="small"
                className="px-2"
                variant="contained"
                onClick={(e) =>{
                  updateResource(id_resource, resourceDispatch);}}
              >
                {status}
              </Button>
            </TableCell>
          </TableRow>
        ))}
      </TableBody>
    </Table>
  );
}

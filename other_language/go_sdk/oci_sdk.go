// This is an automatically generated code sample.
// To make this code sample work in your Oracle Cloud tenancy,
// please replace the values for any parameters whose current values do not fit
// your use case (such as resource IDs, strings containing ‘EXAMPLE’ or ‘unique_id’, and
// boolean, number, and enum parameters with values not fitting your use case).

package main

import (
	"context"
	"fmt"

	"github.com/oracle/oci-go-sdk/v65/common"
	"github.com/oracle/oci-go-sdk/v65/example/helpers"
	"github.com/oracle/oci-go-sdk/v65/functions"
)

func ExampleGetApplication() {
	// Create a default authentication provider that uses the DEFAULT
	// profile in the configuration file.
	// Refer to <see href="https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File>the public documentation</see> on how to prepare a configuration file.
	client, err := functions.NewFunctionsManagementClientWithConfigurationProvider(common.DefaultConfigProvider())
	helpers.FatalIfError(err)

	// Create a request and dependent object(s).

	req := functions.GetApplicationRequest{ApplicationId: common.String("ocid1.compartment.oc1..aaaaaaaajyvcxbeipsa5s4jgzdi7o3oztfqpgxickubwkajwku5hfh4octoq"),
		OpcRequestId: common.String("EJ9TGURIT3LBZZY4FMVU<unique_ID>")}

	// Send the request using the service client
	resp, err := client.GetApplication(context.Background(), req)

	helpers.FatalIfError(err)

	// Retrieve value from the response.
	fmt.Println(resp)
}

func ListApps(){
	provider := common.DefaultConfigProvider()
	client, err := functions.NewFunctionsManagementClientWithConfigurationProvider(provider)
	if err != nil {
		fmt.Println("Error creating Functions client:", err)
		return
	}

	request := functions.ListApplicationsRequest{
		CompartmentId: common.String("ocid1.compartment.oc1..aaaaaaaajyvcxbeipsa5s4jgzdi7o3oztfqpgxickubwkajwku5hfh4octoq"),
	}

	response, err := client.ListApplications(context.Background(), request)
	if err != nil {
		fmt.Println("Error listing applications:", err)
		return
	}

	for _, app := range response.Items {
		fmt.Println("Function Application:", *app.DisplayName)
	}
}

func ExampleGetFunction() {
	// Create a default authentication provider that uses the DEFAULT
	// profile in the configuration file.
	// Refer to <see href="https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File>the public documentation</see> on how to prepare a configuration file.
	client, err := functions.NewFunctionsManagementClientWithConfigurationProvider(common.DefaultConfigProvider())
	helpers.FatalIfError(err)

	// Create a request and dependent object(s).

	req := functions.GetFunctionRequest{FunctionId: common.String("ocid1.test.oc1..<unique_ID>EXAMPLE-functionId-Value"),
		OpcRequestId: common.String("I5P2HYDI20PXPOHSLWZV<unique_ID>")}

	// Send the request using the service client
	resp, err := client.GetFunction(context.Background(), req)
	helpers.FatalIfError(err)

	// Retrieve value from the response.
	fmt.Println(resp)
}

func ExampleCreateApplication() {
	// Create a default authentication provider that uses the DEFAULT
	// profile in the configuration file.
	// Refer to <see href="https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File>the public documentation</see> on how to prepare a configuration file.
	client, err := functions.NewFunctionsManagementClientWithConfigurationProvider(common.DefaultConfigProvider())
	helpers.FatalIfError(err)

	// Create a request and dependent object(s).

	req := functions.CreateApplicationRequest{CreateApplicationDetails: functions.CreateApplicationDetails{
		DisplayName: common.String("app_go_sdk"),
		Shape:       functions.CreateApplicationDetailsShapeArm,
		SubnetIds:   []string{"ocid1.subnet.oc1.ap-singapore-1.aaaaaaaar52xo6nji5vauz3bev24rdeioiq6s6ciixwav7wtrqaepungibva"},
		CompartmentId: common.String("ocid1.compartment.oc1..aaaaaaaajyvcxbeipsa5s4jgzdi7o3oztfqpgxickubwkajwku5hfh4octoq")}}

	// Send the request using the service client
	resp, err := client.CreateApplication(context.Background(), req)
	helpers.FatalIfError(err)

	// Retrieve value from the response.
	fmt.Println(resp)
}


func main() {
    //ExampleCreateApplication()
	ListApps()
}
package main

import (
	"context"
	"fmt"
	"io/ioutil"
	"strings"

	"github.com/oracle/oci-go-sdk/v65/common"
	"github.com/oracle/oci-go-sdk/v65/example/helpers"
	"github.com/oracle/oci-go-sdk/v65/objectstorage"
)

func ExampleListObjects() {
	client, err := objectstorage.NewObjectStorageClientWithConfigurationProvider(common.DefaultConfigProvider())
	helpers.FatalIfError(err)

	// Create a request and dependent object(s).

	req := objectstorage.ListObjectsRequest{
		BucketName:         common.String("Luka-bucket"),
		NamespaceName:      common.String("sehubjapacprod"),
	}

	// Send the request using the service client
	resp, err := client.ListObjects(context.Background(), req)
	helpers.FatalIfError(err)

	// Retrieve value from the response.
	fmt.Println(resp)
}

func ExamplePutObject() {
	// Create a default authentication provider that uses the DEFAULT
	// profile in the configuration file.
	// Refer to <see href="https://docs.cloud.oracle.com/en-us/iaas/Content/API/Concepts/sdkconfig.htm#SDK_and_CLI_Configuration_File>the public documentation</see> on how to prepare a configuration file.
	client, err := objectstorage.NewObjectStorageClientWithConfigurationProvider(common.DefaultConfigProvider())
	helpers.FatalIfError(err)

	// Create a request and dependent object(s).

	req := objectstorage.PutObjectRequest{
		PutObjectBody:           ioutil.NopCloser(strings.NewReader("aWVVDiE92ojKVS7RX9Yr")),
		NamespaceName:           common.String("sehubjapacprod"),
		ObjectName:              common.String("go_object"),
		BucketName:              common.String("Luka-bucket"),}

	// Send the request using the service client
	resp, err := client.PutObject(context.Background(), req)
	helpers.FatalIfError(err)

	// Retrieve value from the response.
	fmt.Println(resp)
}

func ExampleGetObject() {
	client, err := objectstorage.NewObjectStorageClientWithConfigurationProvider(common.DefaultConfigProvider())
	helpers.FatalIfError(err)

	// Create a request and dependent object(s).

	req := objectstorage.GetObjectRequest{
		ObjectName:                     common.String("go_object"),
		BucketName:                     common.String("Luka-bucket"),
		NamespaceName:                  common.String("sehubjapacprod"),
	}

	// Send the request using the service client
	resp, err := client.GetObject(context.Background(), req)
	helpers.FatalIfError(err)

	// Retrieve value from the response.
	fmt.Println(resp)
}

func ExampleDeleteObject() {
	client, err := objectstorage.NewObjectStorageClientWithConfigurationProvider(common.DefaultConfigProvider())
	helpers.FatalIfError(err)

	req := objectstorage.DeleteObjectRequest{
		NamespaceName: common.String("sehubjapacprod"),
		ObjectName:         common.String("go_object"),
		BucketName:         common.String("Luka-bucket"),
		}

	// Send the request using the service client
	resp, err := client.DeleteObject(context.Background(), req)
	helpers.FatalIfError(err)

	// Retrieve value from the response.
	fmt.Println(resp)
}

func main() {
    // ExampleListObjects()
	// ExamplePutObject()
	// ExampleGetObject()
	ExampleDeleteObject()
}
package main

import (
	"context"
	"fmt"

	"github.com/oracle/oci-go-sdk/v65/common"
	"github.com/oracle/oci-go-sdk/v65/example/helpers"
	"github.com/oracle/oci-go-sdk/v65/objectstorage"
)

func ExampleListBuckets() {
	client, err := objectstorage.NewObjectStorageClientWithConfigurationProvider(common.DefaultConfigProvider())
	helpers.FatalIfError(err)

	// Create a request and dependent object(s).

	req := objectstorage.ListBucketsRequest{Limit: common.Int(765),
		NamespaceName:      common.String("sehubjapacprod"),
		CompartmentId:      common.String("ocid1.compartment.oc1..aaaaaaaajyvcxbeipsa5s4jgzdi7o3oztfqpgxickubwkajwku5hfh4octoq"),
		Fields:             []objectstorage.ListBucketsFieldsEnum{objectstorage.ListBucketsFieldsTags}}

	// Send the request using the service client
	resp, err := client.ListBuckets(context.Background(), req)
	helpers.FatalIfError(err)

	// Retrieve value from the response.
	fmt.Println(resp)
}

func ExampleCreateBucket() {
	client, err := objectstorage.NewObjectStorageClientWithConfigurationProvider(common.DefaultConfigProvider())
	helpers.FatalIfError(err)


	req := objectstorage.CreateBucketRequest{
		CreateBucketDetails: objectstorage.CreateBucketDetails{
			Name: common.String("bucket_by_go_sdk"),
		    CompartmentId:      common.String("ocid1.compartment.oc1..aaaaaaaajyvcxbeipsa5s4jgzdi7o3oztfqpgxickubwkajwku5hfh4octoq")},
		    NamespaceName:      common.String("sehubjapacprod"),
		}

	// Send the request using the service client
	resp, err := client.CreateBucket(context.Background(), req)
	helpers.FatalIfError(err)

	// Retrieve value from the response.
	fmt.Println(resp)
}

func ExampleDeleteBucket() {
	client, err := objectstorage.NewObjectStorageClientWithConfigurationProvider(common.DefaultConfigProvider())
	helpers.FatalIfError(err)

	// Create a request and dependent object(s).

	req := objectstorage.DeleteBucketRequest{
		BucketName:    common.String("bucket_by_go_sdk"),
		NamespaceName: common.String("sehubjapacprod")}

	// Send the request using the service client
	resp, err := client.DeleteBucket(context.Background(), req)
	helpers.FatalIfError(err)

	// Retrieve value from the response.
	fmt.Println(resp)
}

func ExampleGetBucket() {
	client, err := objectstorage.NewObjectStorageClientWithConfigurationProvider(common.DefaultConfigProvider())
	helpers.FatalIfError(err)

	// Create a request and dependent object(s).

	req := objectstorage.GetBucketRequest{
		BucketName: common.String("Luka-bucket"),
		NamespaceName:      common.String("sehubjapacprod"),
	}

	// Send the request using the service client
	resp, err := client.GetBucket(context.Background(), req)
	helpers.FatalIfError(err)

	// Retrieve value from the response.
	fmt.Println(resp)
}

func main() {
    // ExampleListBuckets()
	// ExampleCreateBucket()
	// ExampleDeleteBucket()
	ExampleGetBucket()
}
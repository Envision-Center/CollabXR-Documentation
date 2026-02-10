import { ListObjectsV2Command, S3Client } from "@aws-sdk/client-s3";
const client = new S3Client({});

const baseRepoStruct = {
	StructVersion: 1,
	BaseURL: "https://my-bucket.s3.amazonaws.com/",
	RepoName: "My Mod Repository",
	RepoOwner: "My Name",

	S3BucketName: "my-bucket",

	CognitoURL: "cognito-idp.us-east-1.amazonaws.com/",
	CognitoUserPool: "enter-your-user-pool-id",
	CognitoClientID: "272q6v02f9p848r427nko3vmkh",
	CognitoIdentityPool: "enter-your-identity-pool-id",
};

export const handler = async (event) => {
	try {
		const listResponse = await client
			.send(
				new ListObjectsV2Command({
					Bucket: baseRepoStruct.S3BucketName,
				}),
			)
			.catch((e) => {
				return {
					statusCode: 500,
				};
			});

		return {
			statusCode: 200,
			body: {
				...baseRepoStruct,
				Mods: listResponse.Contents.filter((entry) =>
					entry.Key.includes("meta"),
				).map((entry) => entry.Key.split(".")[0]),
			},
		};
	} catch (e) {
		return {
			statusCode: 500,
			body: e.message,
		};
	}
};

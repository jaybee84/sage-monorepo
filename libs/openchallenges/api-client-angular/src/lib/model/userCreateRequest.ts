/**
 * OpenChallenges REST API
 * No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)
 *
 * The version of the OpenAPI document: 1.0.0
 * 
 *
 * NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).
 * https://openapi-generator.tech
 * Do not edit the class manually.
 */


/**
 * The information required to create a user account
 */
export interface UserCreateRequest { 
    login: string;
    /**
     * An email address.
     */
    email: string;
    password: string;
    name?: string | null;
    avatarUrl?: string | null;
    bio?: string | null;
}


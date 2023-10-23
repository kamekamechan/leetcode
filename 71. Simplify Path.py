class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path.split('/')

        output_path = []
        output = ""
        check_array = ["..", ".", ""]

        for directory in path:
            if(directory not in check_array):
                output_path.append(directory)
            elif(directory == ".." and output_path != []):
                output_path.pop()
            else:
                continue
            
        for directory in output_path:
            output += "/" + directory

        if output == "":
            return "/"
        return output

test = Solution()
print(test.simplifyPath("/a/./b/../../c/"))
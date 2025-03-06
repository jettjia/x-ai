/*
 * Copyright 2025 CloudWeGo Authors
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

package knowledgeindexing

import (
	"context"

	"github.com/cloudwego/eino-ext/components/document/loader/file"
	"github.com/cloudwego/eino/components/document"
)

func defaultFileLoaderConfig(ctx context.Context) (*file.FileLoaderConfig, error) {
	config := &file.FileLoaderConfig{}
	return config, nil
}

func NewFileLoader(ctx context.Context, config *file.FileLoaderConfig) (ldr document.Loader, err error) {
	if config == nil {
		config, err = defaultFileLoaderConfig(ctx)
		if err != nil {
			return nil, err
		}
	}
	ldr, err = file.NewFileLoader(ctx, config)
	if err != nil {
		return nil, err
	}
	return ldr, nil
}
